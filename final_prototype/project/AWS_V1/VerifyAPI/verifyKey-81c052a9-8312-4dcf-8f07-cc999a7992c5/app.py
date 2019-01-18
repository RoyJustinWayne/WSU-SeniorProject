import sys
import logging
import rds_config
import pymysql
import json
#rds settings 
rds_host  = rds_config.db_host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name


logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    # sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """
    print("event type-->", type(event))
    print("event==> ",event)
    req = event['body']
    print("req", req)
    loaded_req = json.loads(req)
    apikey = loaded_req['key']
    print("loaded==> ", apikey)

    # item_count = 0
    with conn.cursor() as cur:
        cur.execute("select COUNT(apikey) from stations where apikey='"+str(apikey)+"'")
        
        # cur.execute("create table Employee3 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")  
        # cur.execute('insert into Employee3 (EmpID, Name) values(1, "Joe")')
        # cur.execute('insert into Employee3 (EmpID, Name) values(2, "Bob")')
        # cur.execute('insert into Employee3 (EmpID, Name) values(3, "Mary")')
        # conn.commit()
        # cur.execute("select * from Employee3")
        # print("result-->",result)
        # fetch = cur.fetchall()
        # print(fetch)
        for row in cur:
            print("ROW-->",row[0])
            result = row[0]
            
    conn.commit()
    if (result == 1):
        return {
        "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        "statusCode": 200,
        "body": json.dumps("200")
        }
    else:
        return {
        "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        "statusCode": 400,
        "body": json.dumps("400")
        }