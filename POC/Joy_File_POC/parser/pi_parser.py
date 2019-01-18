import csv 
from datetime import datetime
from sql import WeatherData, db

db.create_all()

with open ('sensor_data.txt', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:

        nondec, frag = line[0].split(".")
       
        date = datetime.strptime(nondec, "%Y-%m-%d %H:%M:%S")

        # time, apiKey, temp, humidity, pressure, latitude, longitude
        apiKey = line[1]
        temp = line[2]
        humidity = line[3]
        pressure = line[4]
        latitude = line[5]
        longitude = line[6]
        
        data = WeatherData(date, apiKey, temp, humidity, pressure, latitude, longitude)
        db.session.add(data)
        db.session.commit()




