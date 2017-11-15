import weather_non_exec
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import pyowm
import json
import requests




class Weather_class(weather_non_exec.Ui_weather_screen, QtWidgets.QWidget):

    def __init__(self):
        super(Weather_class, self).__init__()
        self.setupUi(self)
        self.display_weather()

    def display_weather(self):
        #owm = pyowm.OWM('c51dfb366753c6bd106070bfbbf33196')

        # API KEY - c51dfb366753c6bd106070bfbbf33196   ,   3bf167629aed01d3099123b21f336e10
        # http://api.openweathermap.org/data/2.5/weather?lat=22.569719&lon=88.36972&appid=c51dfb366753c6bd106070bfbbf33196
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


        # observation = owm.weather_at_place("Kolkata,in")
        # w = observation.get_weather()
        # decoded_w = json.loads(w.to_JSON())
        # detailed_status = decoded_w['detailed_status']
        #
        # freegeoip = "http://freegeoip.net/json"
        # geo_r = requests.get(freegeoip)
        # geo_json = geo_r.json()
        #
        # user_postition = geo_json["city"]
        # user_postition = [geo_json["latitude"], geo_json["longitude"]]
        # print(user_postition)



        # strMsg = user_postition + " " + detailed_status.title() + '\n' + str(
        #     decoded_w['humidity']) + '% humidity  ' + '\n' + str(decoded_w['clouds']) + '% cloud'
        # print(strMsg)
        #
        # temperature = w.get_temperature('celsius')
        # tomorrow = pyowm.timeutils.tomorrow()
        # wind = w.get_wind()





        api_address='http://api.openweathermap.org/data/2.5/weather?appid=cd763d1cc74bd82bdbe1381ad4af4f6b&q=Kolkata'

        url = api_address

        json_data = requests.get(url).json()
        location = json_data['name']
        print ('Location:',location)

        temperature = (json_data['main'] ['temp'])-273
        temperature = round(temperature,2)
        print ('Temperature:',temperature,'°C')

        sky_condition = json_data['weather'] [0] ['description']
        print ('Sky Condition:',sky_condition)

        humidity = json_data['main'] ['humidity']
        print ('Humidity:',humidity)

        wind_speed = json_data['wind'] ['speed']
        print ('Wind Speed:',wind_speed)




        if str(sky_condition) == 'haze':
            pixmap = QtGui.QPixmap('haze.png')
            self.weather_image.setPixmap(pixmap)
            self.weather_image.setScaledContents(True)
        elif str(sky_condition) == 'cloudy':
            pixmap = QtGui.QPixmap('cloudy.png')
            self.weather_image.setPixmap(pixmap)
            self.weather_image.setScaledContents(True)
        elif str(sky_condition) == 'light rain':
            pixmap = QtGui.QPixmap('rainy.png')
            self.weather_image.setPixmap(pixmap)
            self.weather_image.setScaledContents(True)
        else:
            pixmap = QtGui.QPixmap('sunny.png')
            self.weather_image.setPixmap(pixmap)
            self.weather_image.setScaledContents(True)


        # print(w)
        # print(str(wind['speed']) + str(" km/hour"))
        # print(str(temperature['temp']) + str(' °C'))
        # print(tomorrow)


        self.value_location.setText(location)
        self.value_temperature.setText(str(temperature) + str(' °C'))
        self.value_humidity.setText(str(humidity) + str(' %'))
        self.value_skycondition.setText(sky_condition)
        self.value_windspeed.setText(str(wind_speed) + str(" km/hr"))



if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    qapp.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    weather_obj = Weather_class()
    weather_obj.show()
    qapp.exec_()
