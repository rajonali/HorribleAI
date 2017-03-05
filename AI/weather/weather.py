import urllib3
import re
import json
import requests
import os

'''
Obtain json to parse from the weather underground api and create readable string to input into espeak.
'''

url = "http://api.wunderground.com/api/c531f3e5a81e8da4/conditions/q/LA/Baton_Rouge.json"

def outputWeather():
    data = requests.get(url).json()
    output = 'The weather in %s, %s is %s and is %s. Humidity levels are at %s.' %(data['current_observation']['display_location']['city'], data['current_observation']['display_location']['state_name'], data['current_observation']['weather'], data['current_observation']['temperature_string'], data['current_observation']['relative_humidity'])
    return output


os.system("espeak '%s'" % outputWeather())
