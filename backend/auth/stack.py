from aws_cdk import (
    Stack,
    aws_cognito as cognito,
    aws_iam as iam,
    aws_lambda as lambda_,
)
from constructs import Construct

class AuthenticationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Pre signup function to limit who can register
        pre_signup_lambda = lambda_.Function(
            self,
            "PreSignUpLambda",
            function_name=f'{self.stack_name}-pre-signup-function',
            runtime=lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_asset("backend/auth/lambda"),
            handler="pre-signup.handler",
        )

        # Create a Cognito User Pool
        user_pool = cognito.UserPool(
            self, 
            "UserPool",
            user_pool_name=f'{self.stack_name}-user-pool',
            sign_in_aliases=cognito.SignInAliases(
                email=True
            ),
            auto_verify=cognito.AutoVerifiedAttrs(
                email=True
            ),
            self_sign_up_enabled=True,
        )

        # Attach the Pre Sign-up Lambda trigger to the User Pool
        user_pool.add_trigger(
            cognito.UserPoolOperation.PRE_SIGN_UP, 
            pre_signup_lambda
        )


        # Create a User Pool Client
        user_pool_client = cognito.UserPoolClient(
            self, 
            "UserPoolClient",
            user_pool=user_pool,
            generate_secret=False
        )

        # Create an Identity Pool
        identity_pool = cognito.CfnIdentityPool(
            self,
            "IdentityPool",
            identity_pool_name=f'{self.stack_name}-identity-pool',
            allow_unauthenticated_identities=False,
            cognito_identity_providers=[
                cognito.CfnIdentityPool.CognitoIdentityProviderProperty(
                    client_id=user_pool_client.user_pool_client_id,
                    provider_name=user_pool.user_pool_provider_name
                )
            ],
        )