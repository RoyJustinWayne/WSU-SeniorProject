from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://endpoint:port/pi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class WeatherData(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # time, apiKey, temp, humidity, pressure, latitude, longitude
    time = db.Column(db.String(80), unique = False)
    apiKey = db.Column(db.String(80), unique = False)
    temp = db.Column(db.String(80), unique = False)
    humidity = db.Column(db.String(80), unique = False)
    pressure = db.Column(db.String(80), unique = False)
    latitude = db.Column(db.String(80), unique = False)
    longitude = db.Column(db.String(80), unique = False)

    def __init__(self, time, apiKey, temp, humidity, pressure, latitude, longitude):
        self.time = time
        self.apiKey = apiKey
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.latitude = latitude
        self.longitude = longitude
