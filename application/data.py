#This is a module that contains functions to be used in my
#Weather app UI

import requests
from datetime import datetime

def hourly_data_list():
    return [ ("Time", "datetime"), ("Temperature", "temp"), ("Heat Index", "feelslike"),
            ("Humidity", "humidity"), ("Dew Point", "dew"), ("Precipitation", "precip"),
            ("Precipitation Probability", "precipprob"), ("Precipitation Type", "preciptype"),
            ("Wind Gust", "windgust"), ("Wind Speed", "windspeed"), ("Wind Direction", "winddir"),
            ("Pressure", "pressure"), ("Visibility", "visibility"), ("Cloud Cover", "cloudcover"),
            ("Solar Radiation", "solarradiation"), ("Solar Energy", "solarenergy"),
            ("UV Index", "uvindex"), ("Severe Risk", "severerisk"), ("Conditions", "conditions")
        ]

def daily_data_list():
    return [("Date", "datetime"), ("Temp Max", "tempmax"),
            ("Temp Min", "tempmin"), ("Temperature", "temp"), ("Feels Like Max", "feelslikemax"),
            ("Feels Like Min", "feelslikemin"), ("Feels Like", "feelslike"), ("Dew Point", "dew"),
            ("Humidity", "humidity"), ("Precipitation", "precip"), ("Precipitation Probability", "precipprob"),
            ("Precipitation Cover", "precipcover"), ("Precipitation Type", "preciptype"),
            ("Wind Gust", "windgust"), ("Wind Speed", "windspeed"), ("Wind Direction", "winddir"),
            ("Pressure", "pressure"), ("Cloud Cover", "cloudcover"),("Visibility", "visibility"),
            ("Solar Radiation", "solarradiation"), ("Solar Energy", "solarenergy"), ("UV Index", "uvindex"),
            ("Severe Risk", "severerisk"), ("Sunrise", "sunrise"), ("Sunset", "sunset"), ("Moon Phase", "moonphase"), 
            ("Conditions", "conditions")
        ]

def get_hourly_update():
    id = str(datetime.now().time())
    url = "http://127.0.0.1:5000/daily_update/{}".format(id[:2]) #request the hourly data exposed by api.py
    hourly_data = requests.get(url)

    if hourly_data.status_code == 200:
        return True, hourly_data.json() #if the request is succesful return a true with the data in dictionary format
    else:
        return False, str(hourly_data.status_code) #if request fails return false with the error code

def get_daily_update():
    url = "http://127.0.0.1:5000/daily_update".format(get_ip())
    daily_data = requests.get(url) #request the daily data exposed by api.py

    if daily_data.status_code == 200:
        return True, daily_data.json()
    else:
        return False, str(daily_data.status_code)
