import json
import urllib.request
import urllib.error


def lambda_handler(event, context):
    # TODO implement
    status = ""
    res = ""
    try:
        status = urllib.request.urlopen("http://loadbalancer-joy-83083793.us-east-2.elb.amazonaws.com/").getcode()
    except Exception as e:
        print(e)
        status == 503
        
    if status == 200:
        res = "Ok"
        print("Ok")
    else:
        res = "Not Ok "
        print("Not Ok")
    
    return {
        "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        "statusCode": 200,
        "body": json.dumps({'server': res})
    }
