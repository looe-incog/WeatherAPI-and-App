import weather
from flask import Flask
from flask import Response
import json

#This code is heavily based on Caleb Curry's REST API Crash Course - Introduction + Full Python API Tutorial
#Here's the link if you are interested: https://www.youtube.com/watch?v=qbLc5a9jdXo. Please do support him.

app = Flask(__name__) #setup flask

@app.route('/') #Creates an endpoint (a root, basically) that "displays" Weather Database when you go to 
                #http://<your_device_ip or loopback address>:5000/
def index():
    return "Weather Database"

@app.route('/daily_update', methods=['GET']) #Creates an endpoint that displays the weather update for the
                                             #current day in json format when you go to 
                                             #http://<your_device_ip or loopback address>:5000/daily_update
def get_daily_update():
    request_daily_update = weather.get_weather() #call the weather module which contains get_weather function
                                                 #that returns weather_data if it succesfully requests it from
                                                 #visual crossing or if it already exists in redis cache
    if request_daily_update[0]:
        return Response(
            json.dumps(request_daily_update[1]["days"][0], sort_keys=False), #returns dictionary
            mimetype="application/json"
        )
    else:
        return request_daily_update[0]

@app.route('/daily_update/<string:id_>', methods=['GET']) #this follows the same functionality as that of get_daily
                                                          #update except that it returns the data of the current hour
def get_hourly_update(id_):
    request_hourly_update = weather.get_weather()
    hourly_id = weather.hourly_id() 

    if request_hourly_update[0]:
        return Response(
            json.dumps(request_hourly_update[1]["days"][0]["hours"][hourly_id[id_]], sort_keys=False), #returns dictionary
            mimetype="application/json"
        )
    else:
        return request_hourly_update[0]