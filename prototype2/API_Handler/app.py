import logging
import rds_config
import pymysql
import json

#rds configurations
rds_host  = rds_config.db_host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

# just for logging activities 
logger = logging.getLogger()
logger.setLevel(logging.INFO)

ok_response = """{
        "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        "statusCode": 200,
        "body": "success"
        }"""

bad_response = """{
        "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        "statusCode": 400,
        "body": "invalid"
        }"""

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):
    """
    fetch data from mysql RDS instance
    """

    #extract the event body 
    req = event['body']
    # load the request
    loaded_req = json.loads(req)
    # get the api key
    apikey = loaded_req['key']
    # stringify the api key for query purpose
    _apikey = str(apikey)
 
    with conn.cursor() as cur:
        cur.execute("select COUNT(apikey) from stations where apikey='"+_apikey+"'")
        # iterate through the object cursor
        for row in cur:
            result = row[0]
            
    conn.commit()

    if (result == 1):
        return ok_response
    else:
        return bad_response