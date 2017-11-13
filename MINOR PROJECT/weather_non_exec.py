# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_app.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_weather_screen(object):
    def setupUi(self, weather_screen):
        weather_screen.setObjectName("weather_screen")
        weather_screen.resize(1083, 508)
        weather_screen.setStyleSheet("background-color: rgb(255,255,255);")
        #weather_screen.setStyleSheet("background-image: url(green-wallpaper.jpg)")
        self.weather_image = QtWidgets.QLabel(weather_screen)
        self.weather_image.setGeometry(QtCore.QRect(720, 100, 311, 291))
        #self.weather_image.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.weather_image.setText("")
        self.weather_image.setObjectName("weather_image")
        self.layoutWidget = QtWidgets.QWidget(weather_screen)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 50, 651, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_location = QtWidgets.QLabel(self.layoutWidget)
        self.label_location.setStyleSheet("font: 20pt \"Rockwell\";")
        self.label_location.setObjectName("label_location")
        self.gridLayout.addWidget(self.label_location, 0, 0, 1, 1)
        self.value_location = QtWidgets.QLabel(self.layoutWidget)
        self.value_location.setStyleSheet("font: 75 italic 18pt \"Consolas\";")
        self.value_location.setText("")
        self.value_location.setAlignment(QtCore.Qt.AlignCenter)
        self.value_location.setObjectName("value_location")
        self.gridLayout.addWidget(self.value_location, 0, 1, 1, 1)
        self.label_temperature = QtWidgets.QLabel(self.layoutWidget)
        self.label_temperature.setStyleSheet("font: 20pt \"Rockwell\";")
        self.label_temperature.setObjectName("label_temperature")
        self.gridLayout.addWidget(self.label_temperature, 1, 0, 1, 1)
        self.value_temperature = QtWidgets.QLabel(self.layoutWidget)
        self.value_temperature.setStyleSheet("font: 75 italic 18pt \"Consolas\";")
        self.value_temperature.setText("")
        self.value_temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.value_temperature.setObjectName("vaue_temperature")
        self.gridLayout.addWidget(self.value_temperature, 1, 1, 1, 1)
        self.label_skycondition = QtWidgets.QLabel(self.layoutWidget)
        self.label_skycondition.setStyleSheet("font: 20pt \"Rockwell\";")
        self.label_skycondition.setObjectName("label_skycondition")
        self.gridLayout.addWidget(self.label_skycondition, 2, 0, 1, 1)
        self.value_skycondition = QtWidgets.QLabel(self.layoutWidget)
        self.value_skycondition.setStyleSheet("font: 75 italic 18pt \"Consolas\";")
        self.value_skycondition.setText("")
        self.value_skycondition.setAlignment(QtCore.Qt.AlignCenter)
        self.value_skycondition.setObjectName("value_skycondition")
        self.gridLayout.addWidget(self.value_skycondition, 2, 1, 1, 1)
        self.label_humidity = QtWidgets.QLabel(self.layoutWidget)
        self.label_humidity.setStyleSheet("font: 20pt \"Rockwell\";")
        self.label_humidity.setObjectName("label_humidity")
        self.gridLayout.addWidget(self.label_humidity, 3, 0, 1, 1)
        self.value_humidity = QtWidgets.QLabel(self.layoutWidget)
        self.value_humidity.setStyleSheet("font: 75 italic 18pt \"Consolas\";")
        self.value_humidity.setText("")
        self.value_humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.value_humidity.setObjectName("value_humidity")
        self.gridLayout.addWidget(self.value_humidity, 3, 1, 1, 1)
        self.label_windspeed = QtWidgets.QLabel(self.layoutWidget)
        self.label_windspeed.setStyleSheet("font: 20pt \"Rockwell\";")
        self.label_windspeed.setObjectName("label_windspeed")
        self.gridLayout.addWidget(self.label_windspeed, 4, 0, 1, 1)
        self.value_windspeed = QtWidgets.QLabel(self.layoutWidget)
        self.value_windspeed.setStyleSheet("font: 75 italic 18pt \"Consolas\";")
        self.value_windspeed.setText("")
        self.value_windspeed.setAlignment(QtCore.Qt.AlignCenter)
        self.value_windspeed.setObjectName("value_windspeed")
        self.gridLayout.addWidget(self.value_windspeed, 4, 1, 1, 1)

        self.retranslateUi(weather_screen)
        QtCore.QMetaObject.connectSlotsByName(weather_screen)

    def retranslateUi(self, weather_screen):
        _translate = QtCore.QCoreApplication.translate
        weather_screen.setWindowTitle(_translate("weather_screen", "Weather"))
        weather_screen.setWindowIcon(QtGui.QIcon('weather-icon.png'))
        self.label_location.setText(_translate("weather_screen", "Location : "))
        self.label_temperature.setText(_translate("weather_screen", "Temperature : "))
        self.label_skycondition.setText(_translate("weather_screen", "Sky Condition : "))
        self.label_humidity.setText(_translate("weather_screen", "Humidity : "))
        self.label_windspeed.setText(_translate("weather_screen", "Wind Speed : "))


