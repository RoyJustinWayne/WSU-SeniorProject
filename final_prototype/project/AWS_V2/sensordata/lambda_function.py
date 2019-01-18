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
    connection = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5,charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
except Exception as e:
    print(e)
# except:
    # logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    # sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded ")

def db(query, connection):
    with connection.cursor() as cursor:
        print(query)
        cursor.execute(query)
        # print("RESPONSE FROM DB-->>>:", cursor)
        results = cursor.fetchall()
        print("DELETE_RESULTS-->>",results)
        # for row in cur:
            # print("ROW-->",row)
            # result = row[0]
    connection.commit()


def do_work(line):
    try:
        connection = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5,charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
    try:
        res = parser(line)
    except Exception as e:
        print("errror occured while parsing")
    # print(res['date'])
    date = str(res['date'])
    api = str(res['apiKey']).strip()
    temp = str(res['temp']).strip()
    humidity = str(res['humidity']).strip()
    pressure = str(res['pressure']).strip()
    latitude = str(res['latitude']).strip()
    longitude = str(res['longitude']).strip()
    cpu = str(res['cpu']).strip()
    battery = str(res['battery']).strip()
    ram = str(res['ram']).strip()
    tableName = "sensor_type"
    api_length = len(res['apiKey'])
    print("api_length: ", api_length)
    if api_length < 2:
        return {
            "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
            "statusCode": 400,
            "body": json.dumps("INVALID API KEY")
        }
    query = "INSERT INTO "+tableName+" (created_at, temperature, humidity, pressure, latitude, longitude, apikey, cpu_usage, battery, ram_usage) VALUES ("+"'"+date+"','"+temp+"','"+humidity+"','"+pressure+"','"+latitude+"','"+longitude+"','"+api+"','"+cpu+"','"+battery+"','"+ram+"')"
    print("query--->",query)
    # db(query)
    with connection.cursor() as cursor:
        # sql = "SELECT `id`, `password` FROM `users`"
        cursor.execute(query)
        insert_results = cursor.fetchall()
    print("INSERT_RESULTS-->>",insert_results)
    # with conn.cursor() as cur:
    #     print(query)
    #     cur.execute(query)
    #     # for row in cur:
    #     #     print("ROW-->",row[0])
    #     #     result = row[0]
    # conn.commit()
    
    with connection.cursor() as cur:
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_results = cursor.fetchall()
        # for row in cur:
            # print("ROW-->",row[0])
            # result = row[0]
    print("SelectLast_RESULTS-->>",last_results)
    connection.commit

    # print(str(result))
    # res = str(result)
    # DELETE from latestweather where apikey="0d323b1edffbf224c210"; INSERT INTO latestweather (weather_id, apikey) VALUES (299, "0d323b1edffbf224c210");
    delete_latest = "DELETE from latestweather where apikey='"+api+"';"
    print("Delete query-->",delete_latest)
    insert_latest = "INSERT INTO latestweather (weather_id, apikey) VALUES ("+str(last_results)+", '"+api+"');"
    print("Insert query-->",insert_latest)
    # update_query = "DELETE from latestweather where apikey='"+api+"'; INSERT INTO latestweather (weather_id, apikey) VALUES ("+str(result)+", '"+api+"');"
    # update_query= "update latestweather SET weather_id="+res+" where apikey='"+api+"'"
    # print(update_query)
    db(delete_latest,connection)
    db(insert_latest, connection)
    # with conn.cursor() as cur:
    #     cur.execute(update_query)
    #     # cur.execute("update latestweather SET weather_id="+str(result)+" where apikey='"+api+"'")
    # conn.commit
    
    # conn.close()
    return 1
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

def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """
    
    # line= "2018-10-18 19:35:02.066199, 1676ad55bc1235c613f2, 97.58, 50.83, 994.97, 42.362495442, -83.071719216"
    req = event['body']    
    res = do_work(req)
    print(req)
    # print("res-->",res)

    return {
        "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        "statusCode": 200,
        "body": json.dumps("Data posted successfully!")
        }