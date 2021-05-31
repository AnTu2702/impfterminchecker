import re, requests, boto3

def lambda_handler(event, context):

    vaccine = event['vaccine']
    vaccid = event['vaccid']
    baseurl = event['baseurl']
    snsArn = event['snsarn']

    message = f"Bitte sofort Termine für den Impfstoff {vaccine} manuell checken! + f"\r\n\r\n{baseurl}{vaccid}"
    regex = r'(.*)' + re.escape('<div class="panel-body">') + r'(.*)' + re.escape('</div> <div class="panel-footer">') + r'(.*)'

    try:
        response = requests.get(baseurl+vaccid)
        message = re.match(regex, re.sub(' +',' ', response.text.replace("\r\n","").replace("\t"," "))).group(2).strip()
    except:
        boto3.client('sns').publish(TargetArn=snsArn, Message=message, Subject=vaccine)
    finally:
        return f"{vaccine}: {message}"
