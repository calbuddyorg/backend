#!/usr/bin/env python3
import os
import aws_cdk as cdk
import environments
from dotenv import load_dotenv

load_dotenv(override=True)

from backend.auth.stack import AuthenticationStack
from backend.stacks import (
    AnalyticsStack, 
    AuthenticationStack, 
    DataStack, 
    NetworkStack
)

ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME", "DEV")

app = cdk.App()
AuthenticationStack(
    app, 
    "AuthenticationStack",
    description="Authentication Stack for CalBuddy Demo",
    env = environments.engineering[ENVIRONMENT_NAME],
    stack_name=f"calbuddy-auth-{ENVIRONMENT_NAME.lower()}",
)

app.synth()
