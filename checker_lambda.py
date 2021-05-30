import re, requests, boto3

def lambda_handler(event, context):

    vaccine = event['vaccine']
    vaccid = event['vaccid']
    baseurl = event['baseurl']
    snsArn = event['snsarn']

    message = 'Bitte sofort Termine für den Impfstoff ' + vaccine + ' manuell checken!'

    try:
        response = requests.get(baseurl+vaccid)
        regex = r'(.*)' + re.escape('<div class="panel-body">') + r'(.*)' + re.escape('</div> <div class="panel-footer">') + r'(.*)'
        html = re.sub(' +',' ', response.text.replace("\r\n","").replace("\t"," "))
        matchObj = re.match(regex, html)
        message = matchObj.group(2).strip()
    except:
        boto3.client('sns').publish(TargetArn=snsArn, Message=message, Subject=vaccine)
    finally:
        print(f"{baseurl}{vaccid}")
        return f"{vaccine}: {message}"
