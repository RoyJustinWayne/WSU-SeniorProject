import csv 
from datetime import datetime

def parser_helper(line):
    nofrag, frag = line[0].split(".")
    date = datetime.strptime(nofrag, "%Y-%m-%d %H:%M:%S")

    for i in range(len(line)):
        if i == 0:
            nondec, dec = line[0].split(".")
            date = datetime.strptime(nondec, "%Y-%m-%d %H:%M:%S")
        elif i == 1:
            apiKey = line[i]
        elif i == 2:
            temp = line[i]
        elif i == 3:
            humidity = line[i]
        elif i == 4:
            pressure = line[i]
        elif i == 5:
            latitude = line[i]
        elif i == 6:
            longitude = line[i]
    
    print("date: ", date)
    print("apiKey: ", apiKey)
    print("temp: ", temp)
    print("humidity: ", humidity)
    print("pressure: ", pressure)
    print("latitude: ", latitude)
    print("longitude: ", longitude)
    # data = WeatherData(date, apiKey, temp, humidity, pressure, latitude, longitude)
    # db.session.add(data)
    # db.session.commit()
    # print(data)
    return 0

def convertToList(string): 
    line = list(string.split(",")) 
    return line 

def parse(line):
    print("string-->",line)
    new_line = convertToList(line)
    print(new_line)
    parser_helper(new_line)


def lambda_handler(event, context):
    line= "2018-09-18 17:35:02.066199, 28cbe87809185a040a5d, 86.58, 50.83, 994.97, 42.362495442, -83.071719216"
    parse(line)
    return
