from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_iam as iam,
    aws_lambda as lambda_,
)
from constructs import Construct

class NetworkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
