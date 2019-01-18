import json
import datetime
from dateutil import tz

def parser_helper(line):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('EST')
    utc = datetime.datetime.now()
    utc = utc.replace(tzinfo=from_zone)
    etc = utc.astimezone(to_zone)
    new_time = str(etc)
    print("TIME NOW: ", new_time)
    for i in range(len(line)):
        if i == 0:
            nondec, dec = new_time.split(".")
            print("nondec ==>",nondec)
            in_date = nondec
        elif i == 1:
            in_apiKey = line[i]
        elif i == 2:
            in_temp = line[i]
        elif i == 3:
            in_humidity = line[i]
        elif i == 4:
            in_pressure = line[i]
        elif i == 5:
            in_latitude = line[i]
        elif i == 6:
            in_longitude = line[i]
        elif i == 7:
            in_cpu = line[i]
        elif i == 8:
            in_battery = "00:00:00"
        elif i == 9:
            in_ram = line[i]
    
    data = {"date": str(in_date), "apiKey": in_apiKey, "temp": in_temp, "humidity": in_humidity, "pressure": in_pressure, "latitude": in_latitude, "longitude": in_longitude, "cpu": in_cpu, "battery": in_battery, "ram": in_ram}

    json_data = json.dumps(data)

    return json_data

def convertToList(string): 
    line = list(string.split(",")) 
    return line 

def parse(line):
    print("string-->",line)
    new_line = convertToList(line)
    print(new_line)
    data = parser_helper(new_line)
    return data

def parser(line):
    # line= "2018-09-18 17:35:02.066199, 28cbe87809185a040a5d, 86.58, 50.83, 994.97, 42.362495442, -83.071719216"
    ret = parse(line)
    resp = json.loads(ret)
    
    return resp

if __name__=="__main__":
    parser()
