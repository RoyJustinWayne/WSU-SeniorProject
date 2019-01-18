import sys
import logging
import rds_config
import pymysql
import json
#rds settings
from parser import parser

rds_host  = rds_config.db_host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name


logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except Exception as e:
    print(e)
# except:
    # logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    # sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")

def db(query):
    with conn.cursor() as cur:
        print(query)
        cur.execute(query)
        for row in cur:
            print("ROW-->",row[0])
            result = row[0]
    conn.commit()


def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """
    
    line= "2020-10-18 19:35:02.066199, 1676ad55bc1235c613f2, 77.58, 50.83, 994.97, 42.362495442, -83.071719216"
    res = parser(line)
    print(res['date'])
    date = str(res['date'])
    api = str(res['apiKey']).strip()
    temp = str(res['temp']).strip()
    humidity = str(res['humidity']).strip()
    pressure = str(res['pressure']).strip()
    latitude = str(res['latitude']).strip()
    longitude = str(res['longitude']).strip()
    tableName = "weather"
    api_length = len(res['apiKey'])
    print("api_length: ", api_length)
    if api_length < 2:
        return {
            "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
            "statusCode": 400,
            "body": json.dumps("INVALID API KEY")
        }
    query = "INSERT INTO "+tableName+" (created_at, temperature, humidity, pressure, latitude, apikey) VALUES ("+"'"+date+"','"+temp+"','"+humidity+"','"+pressure+"','"+latitude+"','"+api+"')"
    db(query)
    # with conn.cursor() as cur:
    #     print(query)
    #     cur.execute(query)
    #     # for row in cur:
    #     #     print("ROW-->",row[0])
    #     #     result = row[0]
    # conn.commit()
    
    with conn.cursor() as cur:
        cur.execute("SELECT LAST_INSERT_ID()")
        for row in cur:
            print("ROW-->",row[0])
            result = row[0]
    conn.commit
    print(str(result))
    res = str(result)
    update_query= "update latestweather SET weather_id="+res+" where apikey='"+api+"'"
    print(update_query)
    db(update_query)
    # with conn.cursor() as cur:
    #     cur.execute(update_query)
    #     # cur.execute("update latestweather SET weather_id="+str(result)+" where apikey='"+api+"'")
    # conn.commit
    
    conn.close()
    # print("event type-->", type(event))
    # print("event==> ",event)
    # req = event['body']
    # print("req", req)
    # loaded_req = json.loads(req)
    # apikey = loaded_req['key']
    # print("loaded==> ", apikey)


    # with conn.cursor() as cur:
    #     cur.execute("select COUNT(apikey) from stations where apikey='"+str(apikey)+"'")
  
    #     for row in cur:
    #         print("ROW-->",row[0])
    #         result = row[0]
            
    # conn.commit()
    # if (result == 1):
    #     return {
    #     "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
    #     "statusCode": 200,
    #     "body": json.dumps("200")
    #     }
    # else:
    #     return {
    #     "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
    #     "statusCode": 400,
    #     "body": json.dumps("400")
    #     }