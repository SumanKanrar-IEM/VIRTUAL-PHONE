# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(948, 621)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 721, 471))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("font: 75 italic 10pt \"Comic Sans MS\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_contacts = QtWidgets.QWidget()
        self.tab_contacts.setObjectName("tab_contacts")
        self.tableView_contacts = QtWidgets.QTableView(self.tab_contacts)
        self.tableView_contacts.setGeometry(QtCore.QRect(10, 20, 361, 331))
        self.tableView_contacts.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_contacts.setObjectName("tableView_contacts")
        self.btn_backup = QtWidgets.QPushButton(self.tab_contacts)
        self.btn_backup.setGeometry(QtCore.QRect(400, 180, 131, 41))
        self.btn_backup.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.btn_backup.setObjectName("btn_backup")
        self.btn_addcon = QtWidgets.QPushButton(self.tab_contacts)
        self.btn_addcon.setGeometry(QtCore.QRect(400, 110, 131, 41))
        self.btn_addcon.setStyleSheet("border-color: rgb(79, 79, 238);\n"
"alternate-background-color: rgb(0, 170, 255);\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.btn_addcon.setObjectName("btn_addcon")
        self.tabWidget.addTab(self.tab_contacts, "")
        self.tab_voice = QtWidgets.QWidget()
        self.tab_voice.setObjectName("tab_voice")
        self.tableView_voice = QtWidgets.QTableView(self.tab_voice)
        self.tableView_voice.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.tableView_voice.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_voice.setObjectName("tableView_voice")
        self.tabWidget.addTab(self.tab_voice, "")
        self.tab_sms = QtWidgets.QWidget()
        self.tab_sms.setObjectName("tab_sms")
        self.tableView_sms = QtWidgets.QTableView(self.tab_sms)
        self.tableView_sms.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.tableView_sms.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_sms.setObjectName("tableView_sms")
        self.tabWidget.addTab(self.tab_sms, "")
        self.tab_mms = QtWidgets.QWidget()
        self.tab_mms.setObjectName("tab_mms")
        self.tableView_mms = QtWidgets.QTableView(self.tab_mms)
        self.tableView_mms.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.tableView_mms.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_mms.setObjectName("tableView_mms")
        self.tabWidget.addTab(self.tab_mms, "")
        self.tab_email = QtWidgets.QWidget()
        self.tab_email.setObjectName("tab_email")
        self.tableView_email = QtWidgets.QTableView(self.tab_email)
        self.tableView_email.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.tableView_email.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_email.setObjectName("tableView_email")
        self.tabWidget.addTab(self.tab_email, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 331, 101))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 71, 81))
        self.label.setStyleSheet("background-color: none;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("rsz_158142_addressbook_256x256.png"))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Phonebook"))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_backup.setText(_translate("Dialog", "Backup"))
        self.btn_addcon.setText(_translate("Dialog", "Add Contact"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contacts), _translate("Dialog", "     Contacts      "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_voice), _translate("Dialog", "    Voice Message     "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sms), _translate("Dialog", "      SMS      "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mms), _translate("Dialog", "     MMS    "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_email), _translate("Dialog", "     E-mail    "))
        self.label_2.setText(_translate("Dialog", "Phone Book"))
        self.label.setToolTip(_translate("Dialog", "<img src=\"C:\\Users\\USER\\Desktop\\project\" height=\"50\" width=\"30\">"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

