# impfterminchecker
Automatically check and notify (push) for vaccination dates offered via terminland.de

Code may be uploaded as AWS-Lambda (Python 3.x)
<img src="images/aws_lambda_overview.png"/>

AWS-CloudWatchEvent Rules (time triggered) may be used for triggering the AWS-Lambda...
<img src="images/cloudwatch_event.png"/>

Static JSON to be attached to the event...
<img src="images/cloudwatch_event_rule_static_json.png"/>

AWS-SNS will be used for notification...
<img src="images/aws_sns.png"/>
