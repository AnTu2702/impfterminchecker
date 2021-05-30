# impfterminchecker
Automatically check and notify (push) for vaccination dates offered via terminland.de

Code may be uploaded as AWS Lambda (Python 3.x)
<img src="aws_lambda_overview.png"/>

CloudWatch Event Rules (time triggered) may be used for triggering the Lambda...
<img src="cloudwatch_event.png"/>

Static JSON is attached to the event...
<img src="cloudwatch_event_rule_static_json.png"/>

AWS SNS will be used for notification...
<img src="aws_sns.png"/>
