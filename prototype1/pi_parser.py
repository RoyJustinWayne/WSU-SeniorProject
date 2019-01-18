import csv 
from datetime import datetime
from sql import WeatherData, db
from pathlib import Path

def setup():
    db.create_all()

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

    data = WeatherData(date, apiKey, temp, humidity, pressure, latitude, longitude)
    db.session.add(data)
    db.session.commit()
    print(data)
    return data

def parse(f_name):
    with open (f_name, 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            parser_helper(line)
    return 1

def check_exist(f_name):

    f = Path(f_name)

    if f.is_file():
        return True
    else:
        print("No file") 
        return False

def database_health_status():

    output = 'database OK'

    try:
        #this just to check database connection
        db.session()
    except Exception as e:
        output = str(e)

    return output

def pi_parser():

    f_name = 'dataFiles.txt'
    setup() #if the table doesn't already exists
    if check_exist(f_name):
        parse(f_name)
    else:
        print("file check_exist returned false")

if __name__ == '__main__':
    # setup() #if the table doesn't already exists
    pi_parser()