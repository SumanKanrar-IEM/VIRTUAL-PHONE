# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 668)
        Dialog.setStyleSheet("background-image: url(back.png);")

        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 93, 91))
        self.pushButton.setIcon(QtGui.QIcon('browser.png'))
        self.pushButton.setIconSize(QSize(75,75))
        self.pushButton.setStyleSheet('background-color: indica')
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 90, 93, 91))
        self.pushButton_2.setIcon(QtGui.QIcon('phonebook.png'))
        self.pushButton_2.setIconSize(QSize(75, 75))
        self.pushButton_2.setStyleSheet('background-color: indica')
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")


        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 290, 93, 91))
        self.pushButton_3.setIcon(QtGui.QIcon('calender.png'))
        self.pushButton_3.setIconSize(QSize(75, 75))
        self.pushButton_3.setStyleSheet('background-color: indica')
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 290, 93, 91))
        self.pushButton_4.setIcon(QtGui.QIcon('calculator.png'))
        self.pushButton_4.setIconSize(QSize(75, 75))
        self.pushButton_4.setStyleSheet('background-color: indica')
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")


        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 500, 93, 91))
        self.pushButton_5.setIcon(QtGui.QIcon('cloud.png'))
        self.pushButton_5.setIconSize(QSize(75, 75))
        self.pushButton_5.setStyleSheet('background-color: indica')
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")


        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 500, 93, 91))
        self.pushButton_6.setIcon(QtGui.QIcon('notepad.png'))
        self.pushButton_6.setIconSize(QSize(75, 75))
        self.pushButton_6.setStyleSheet('background-color: indica')
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Homescreen"))
        Dialog.setWindowIcon(QtGui.QIcon('home.png'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

