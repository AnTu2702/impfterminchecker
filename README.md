# impfterminchecker
Automatically check and notify (push) for vaccination dates offered via terminland.de

Code may be uploaded as AWS Lambda (Python 3.x)
<img src="aws_lambda_overview.png"/>

CloudWatch Event Rules (time triggered) may be used with static JSON event data for triggering the Lambda...

AWS SNS will be used for notification...
