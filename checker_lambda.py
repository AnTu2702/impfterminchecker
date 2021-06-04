import re, requests, boto3

def lambda_handler(event, context):

    vaccine = event['vaccine']
    vaccid = event['vaccid']
    baseurl = event['baseurl']
    snsArn = event['snsarn']

    message = f"Bitte sofort Termine für den Impfstoff {vaccine} manuell checken!\r\n\r\n{baseurl}{vaccid}"
    regex = r'(.*)' + re.escape('<div class="panel-body">') + r'(.*)' + re.escape('</div> <div class="panel-footer">') + r'(.*)'

    try:
        response = requests.get(baseurl+vaccid)
        if 'Wartezeit' in response.text:
            rg_min = r'(.*)' + re.escape('<span id="lblMin">') + r'(.*)' + re.escape('</span> Minuten') + r'(.*)'
            rg_sec = r'(.*)' + re.escape('<span id="lblSec">') + r'(.*)' + re.escape('</span> Sekunden') + r'(.*)'
            r_min = re.match(rg_min, re.sub(' +',' ', response.text.replace("\r\n","").replace("\t"," "))).group(2).strip()
            r_sec = re.match(rg_sec, re.sub(' +',' ', response.text.replace("\r\n","").replace("\t"," "))).group(2).strip()
            message = f"Webseite verlangt Wartezeit - Minuten {r_min} Sekunden {r_sec}. Probiere es später wieder..."
        else:
            message = re.match(regex, re.sub(' +',' ', response.text.replace("\r\n","").replace("\t"," "))).group(2).strip()
    except:
        boto3.client('sns').publish(TargetArn=snsArn, Message=message, Subject=vaccine)
    finally:
        print(f"{baseurl}{vaccid}")
        return f"{vaccine}: {message}"
