import requests
import json
import os
city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=0c772cb548ac4cfc97f53950231506&q={city}%27"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = wdic["location"]["region"]
os.system(f"say 'The current weather in {city} is {w} degrees'")