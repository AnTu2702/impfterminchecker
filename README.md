# impfterminchecker
Automatically check for and notify about vaccination dates offered via terminland.de

Code may be uploaded as AWS-Lambda (Python 3.x)
<img src="images/aws_lambda_overview.png"/>

AWS-CloudWatchEvent Rules (time triggered) may be used for triggering the AWS-Lambda...
<img src="images/cloudwatch_event.png"/>

Static JSON to be attached to the event...
<img src="images/cloudwatch_event_rule_static_json.png"/>

AWS-SNS will be used for notification...
<img src="images/aws_sns.png"/>

AWS-SNS Lambda Target Configuration...
<img src="images/aws_lambda_sns_target.png"/>

---

How to find a doctor in your area using terminland...
<img src="images/praxis-finden.png"/>
