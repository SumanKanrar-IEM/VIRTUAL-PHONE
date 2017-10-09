# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_widget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 200)
        Form.setMinimumSize(QtCore.QSize(429, 200))
        Form.setMaximumSize(QtCore.QSize(429, 200))
        Form.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0.4375 rgba(14, 212, 95, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 391, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(11, 21, 58, 18))
        self.label.setMinimumSize(QtCore.QSize(58, 18))
        self.label.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(11, 45, 91, 18))
        self.label_2.setMinimumSize(QtCore.QSize(91, 18))
        self.label_2.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(11, 69, 63, 18))
        self.label_3.setMinimumSize(QtCore.QSize(63, 18))
        self.label_3.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(11, 93, 61, 18))
        self.label_4.setMinimumSize(QtCore.QSize(61, 18))
        self.label_4.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(11, 117, 37, 18))
        self.label_5.setMinimumSize(QtCore.QSize(37, 18))
        self.label_5.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(111, 21, 64, 18))
        self.label_6.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(111, 45, 64, 18))
        self.label_7.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(111, 69, 64, 18))
        self.label_8.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(111, 93, 64, 18))
        self.label_11.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(111, 117, 64, 18))
        self.label_9.setStyleSheet("background-color: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(250, 10, 121, 121))
        self.label_10.setMinimumSize(QtCore.QSize(121, 121))
        self.label_10.setStyleSheet("background-color: none;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("sunny.png"))
        self.label_10.setObjectName("label_10")
        self.label_11.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Location:"))
        self.label_2.setText(_translate("Form", "Temperature:"))
        self.label_3.setText(_translate("Form", "Condition:"))
        self.label_4.setText(_translate("Form", "Humidity:"))
        self.label_5.setText(_translate("Form", "Wind:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

