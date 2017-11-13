# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_contact.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(891, 873)
        Form.setMinimumSize(QtCore.QSize(891, 873))
        Form.setMaximumSize(QtCore.QSize(891, 873))
        Form.setStyleSheet("background-color: rgb(181, 206, 231);")
        self.contact_icon = QtWidgets.QLabel(Form)
        self.contact_icon.setGeometry(QtCore.QRect(310, 30, 251, 191))
        self.contact_icon.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contact_icon.setText("")
        self.contact_icon.setObjectName("contact_icon")
        self.btn_set_icon = QtWidgets.QPushButton(Form)
        self.btn_set_icon.setGeometry(QtCore.QRect(330, 240, 211, 41))
        self.btn_set_icon.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_set_icon.setObjectName("btn_set_icon")
        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setGeometry(QtCore.QRect(50, 330, 111, 51))
        self.name_label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.name_label.setObjectName("name_label")
        self.phone_label = QtWidgets.QLabel(Form)
        self.phone_label.setGeometry(QtCore.QRect(50, 430, 241, 51))
        self.phone_label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.phone_label.setObjectName("phone_label")
        self.email_label = QtWidgets.QLabel(Form)
        self.email_label.setGeometry(QtCore.QRect(50, 530, 161, 51))
        self.email_label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.email_label.setObjectName("email_label")
        self.address_label = QtWidgets.QLabel(Form)
        self.address_label.setGeometry(QtCore.QRect(50, 630, 151, 51))
        self.address_label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.address_label.setObjectName("address_label")
        self.address_textEdit = QtWidgets.QTextEdit(Form)
        self.address_textEdit.setGeometry(QtCore.QRect(500, 630, 371, 51))
        self.address_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 16pt \"Consolas\";")
        self.address_textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.address_textEdit.setObjectName("address_textEdit")
        self.dob_label = QtWidgets.QLabel(Form)
        self.dob_label.setGeometry(QtCore.QRect(50, 730, 221, 51))
        self.dob_label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.dob_label.setObjectName("dob_label")
        self.name_lineEdit = QtWidgets.QLineEdit(Form)
        self.name_lineEdit.setGeometry(QtCore.QRect(500, 330, 371, 51))
        self.name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 16pt \"Consolas\";")
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.phone_lineEdit = QtWidgets.QLineEdit(Form)
        self.phone_lineEdit.setGeometry(QtCore.QRect(500, 430, 371, 51))
        self.phone_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 16pt \"Consolas\";")
        self.phone_lineEdit.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly)
        self.phone_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(Form)
        self.email_lineEdit.setGeometry(QtCore.QRect(500, 530, 371, 51))
        self.email_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 16pt \"Consolas\";")
        self.email_lineEdit.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.dob_dateEdit = QtWidgets.QDateEdit(Form)
        self.dob_dateEdit.setGeometry(QtCore.QRect(630, 730, 241, 51))
        self.dob_dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dob_dateEdit.setAutoFillBackground(False)
        self.dob_dateEdit.setStyleSheet("font: 75 italic 16pt \"Consolas\";\n"
"background-color: rgb(255, 255, 255);")
        self.dob_dateEdit.setInputMethodHints(QtCore.Qt.ImhDate)
        self.dob_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dob_dateEdit.setObjectName("dob_dateEdit")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(330, 810, 211, 41))
        self.btn_save.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(249, 166, 124);\n"
"")
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Contact"))
        self.btn_set_icon.setText(_translate("Form", "Set Contact Icon"))
        self.name_label.setText(_translate("Form", "Name : "))
        self.phone_label.setText(_translate("Form", "Phone Number :"))
        self.email_label.setText(_translate("Form", "Email ID :"))
        self.address_label.setText(_translate("Form", "Address :"))
        self.dob_label.setText(_translate("Form", "Date of Birth :"))
        self.btn_save.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

