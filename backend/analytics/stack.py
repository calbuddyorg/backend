from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
)
from constructs import Construct

class AnalyticsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        