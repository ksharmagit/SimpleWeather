#!pip install requests

import requests
import json
from pprint import pprint

# Get your own key from OWM. There's a free plan as well
# https://home.openweathermap.org/users/sign_up
key = ''

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=23059,us&APPID=' + key)

data = json.loads(r.text)
##pprint(data)

print ("The temperature is", "{0:.3f}".format(((float)(data['main']['temp'])-273)*9/5+32), "F")
print ("The temperature is", "{0:.2f}".format(((float)(data['main']['temp'])-273)), "C")
