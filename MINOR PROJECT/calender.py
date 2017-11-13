# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calender.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(50,50,500,360)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGridVisible(True)


        self.calendarWidget.setGeometry(QtCore.QRect(50, 50, 400, 250))
        self.calendarWidget.setObjectName("calendarWidget")


        self.label = QtWidgets.QLabel(Form)
        date = self.calendarWidget.selectedDate()
        self.label.setText(date.toString())
        self.label.setGeometry(QtCore.QRect(190, 200, 350, 270))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calender"))
        Form.setWindowIcon(QtGui.QIcon('calender.png'))

        self.calendarWidget.setWhatsThis(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">currentdate=bold</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

