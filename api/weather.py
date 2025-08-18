import requests
import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_weather():
    
    if r.get('weather_data'): #Check cache: This checks if weather_data already exists in redis and have not yet expired
        return True, json.loads(r.get('weather_data')) #return the data in a dictionary format
    else:

        #Check response: If the response of redis GET is null or weahter_data does not exist, then it would
        #reques data from visual crossing, then store that data with an expiry of 120 seconds.

        url = "" #paste your own API link from visual crossing here

        response = requests.get(url)
        if response.status_code == 200:
            r.setex('weather_data', 120, json.dumps(response.json()))   #store json file as a string for easier 
                                                                        #checking if exists or not in the redis database
            
            return True, json.loads(r.get('weather_data'))              #return true if request is succesful alogn with the data in dictionary format
        else:
            return False, str(response.status_code)
            #return false if request fails along with the status code

def hourly_id():
    hourly_id = {
                    "00": 0, "01": 1, "02": 2, "03": 3, "04": 4, "05": 5, "06": 6, "07": 7, "08": 8,
                    "09": 9, "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15, "16": 16, "17": 17,
                    "18": 18, "19": 19, "20": 20, "21": 21, "22": 22, "23": 23,
                }
    return hourly_id
