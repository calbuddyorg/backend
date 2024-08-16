#!/usr/bin/env python3
import aws_cdk as cdk

# Hard-coded environments
engineering = {
    "DEV": cdk.Environment(account='654654598073', region='us-east-1'),
    "TESTING": cdk.Environment(account='654654598073', region='us-west-1'),
    "PROD" : cdk.Environment(account='654654598073', region='us-east-2'),
}
