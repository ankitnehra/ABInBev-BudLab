import pyowm
import requests


API_KEY = '2b54876f31212bf7fb13d0d0b62b911d'
COORDS = (40.1164, -88.2434)
#get an owm instance using the key from home.openweathermap.org
owm = pyowm.OWM(API_KEY)

#get current weather
observation = owm.weather_at_coords(COORDS[0], COORDS[1])
weather = observation.get_weather()
temp = weather.get_temperature('celsius')
clouds = weather.get_clouds()
rain = weather.get_rain()
alt = weather.get_pressure()['sea_level']
press = weather.get_pressure()['press']

if len(rain)==0:
    rain = 0
else:
    rain = rain['3h']

print("temperature: "+str(temp['temp'])+'\n' \
      "clouds: "+str(clouds)+'\n' \
      "rain: "+str(rain)+"\n" \
      "altitude: "+str(press))

loc = observation.get_location()
print(loc.get_name())
