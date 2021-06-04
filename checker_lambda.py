import re, requests, boto3

def extract_from(response, lhs, rhs):
    
    regex = r'(.*)' + re.escape(lhs) + r'(.*)' + re.escape(rhs) + r'(.*)'
    string = re.sub(' +',' ', response.text.replace("\r\n","").replace("\t"," "))
    
    return re.match(regex, string).group(2).strip()
    
def lambda_handler(event, context):

    vaccine = event['vaccine']
    vaccid = event['vaccid']
    baseurl = event['baseurl']
    snsArn = event['snsarn']

    message = f"Bitte sofort Termine für den Impfstoff {vaccine} manuell checken!\r\n\r\n{baseurl}{vaccid}"

    try:
        response = requests.get(baseurl+vaccid)
        if 'Wartezeit' in response.text:
            r_min = extract_from(response, '<span id="lblMin">', '</span> Minuten')
            r_sec = extract_from(response, '<span id="lblSec">', '</span> Sekunden')
            message = f"Webseite verlangt Wartezeit - Minuten {r_min} Sekunden {r_sec}. Probiere es später wieder..."
        else:
            message = extract_from(response, '<div class="panel-body">', '</div> <div class="panel-footer">')
    except:
        boto3.client('sns').publish(TargetArn=snsArn, Message=message, Subject=vaccine)
    finally:
        print(f"{baseurl}{vaccid}")
        return f"{vaccine}: {message}"
