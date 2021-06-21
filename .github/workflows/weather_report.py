  
import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

f=open("report.txt","w")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

f.write ("-------------------------------------------------------------")
f.write ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
f.write ("-------------------------------------------------------------")

f.write("Current temperature is: {:.2f} deg C".format(temp_city))
f.write("Current weather desc  :",weather_desc)
f.write("Current Humidity      :",hmdt, '%')
f.write("Current wind speed    :",wind_spd ,'kmph')
f.close()
