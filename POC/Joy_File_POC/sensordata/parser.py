import json
from datetime import datetime

def parser_helper(line):
    nofrag, frag = line[0].split(".")
    date = datetime.strptime(nofrag, "%Y-%m-%d %H:%M:%S")

    for i in range(len(line)):
        if i == 0:
            nondec, dec = line[0].split(".")
            in_date = datetime.strptime(nondec, "%Y-%m-%d %H:%M:%S")
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
    
    # print("date: ", in_date)
    # print("apiKey: ", in_apiKey)
    # print("temp: ", temp)
    # print("humidity: ", humidity)
    # print("pressure: ", pressure)
    # print("latitude: ", latitude)
    # print("longitude: ", longitude)
    
    
    
    data = {"date": str(in_date), "apiKey": in_apiKey, "temp": in_temp, "humidity": in_humidity, "pressure": in_pressure, "latitude": in_latitude, "longitude": in_longitude}

    json_data = json.dumps(data)
    # data = WeatherData(date, apiKey, temp, humidity, pressure, latitude, longitude)
    # db.session.add(data)
    # db.session.commit()
    # print(data)
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
    # print(parsable['date'])
    #returns a parsable json object
    return resp

if __name__=="__main__":
    parser()
