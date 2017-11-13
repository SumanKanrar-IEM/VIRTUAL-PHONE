import pyowm
import json
import requests

owm = pyowm.OWM('c51dfb366753c6bd106070bfbbf33196')

#API KEY - c51dfb366753c6bd106070bfbbf33196   ,   3bf167629aed01d3099123b21f336e10
#http://api.openweathermap.org/data/2.5/weather?lat=22.569719&lon=88.36972&appid=c51dfb366753c6bd106070bfbbf33196
# {
#
#     "id": 1275004,
#
#     "name": "Kolkata",
#
#     "country": "IN",
#
#     "coord": {
#         "lon": 88.36972,
#         "lat": 22.569719
#     }
#
# }


observation = owm.weather_at_place("Kolkata,in")
w = observation.get_weather()
decoded_w = json.loads(w.to_JSON())
detailed_status = decoded_w['detailed_status']

freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()

user_postition = geo_json["city"]
#user_postition = [geo_json["latitude"], geo_json["longitude"]]
#print(user_postition)



strMsg = user_postition +" " + detailed_status.title() + '\n' + str(decoded_w['humidity']) + '% humidity  ' + '\n' + str(decoded_w['clouds']) + '% cloud'
print(strMsg)

temperature = w.get_temperature('celsius')
tomorrow = pyowm.timeutils.tomorrow()
wind = w.get_wind()


#print(w)
print(str(wind['speed']) + str(" km/hour"))
print(str(temperature['temp']) + str(' °C'))
print(tomorrow)