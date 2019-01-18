import requests 
import json

    #used to get wind speed and direction from openweathermap
def appending(dataP): 
    apiKey = "openweatherapi"
    url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="+apiKey+"&units=metrics&q=detroit"

    res = requests.post(url = url) 
    dataJSON = res.text
    loaded = json.loads(dataJSON)
    windSpeed = str(loaded["list"][0]["wind"]["speed"])
    windDeg = str(loaded["list"][0]["wind"]["deg"])
        
    line = dataP.strip('\n')
    line2 = line + ", " + windDeg + ", " + windSpeed
    return line2

        


