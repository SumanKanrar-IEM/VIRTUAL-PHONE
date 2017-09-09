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
        Dialog.resize(730, 621)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 721, 471))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("font: 75 italic 10pt \"Comic Sans MS\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableView = QtWidgets.QTableView(self.tab_5)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 361, 331))
        self.tableView.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView.setObjectName("tableView")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 180, 131, 41))
        self.pushButton_2.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 110, 131, 41))
        self.pushButton_3.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView_2 = QtWidgets.QTableView(self.tab)
        self.tableView_2.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.tableView_2.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_2.setObjectName("tableView_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableView_3 = QtWidgets.QTableView(self.tab_3)
        self.tableView_3.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.tableView_3.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_3.setObjectName("tableView_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView_4 = QtWidgets.QTableView(self.tab_2)
        self.tableView_4.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.tableView_4.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_4.setObjectName("tableView_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableView_5 = QtWidgets.QTableView(self.tab_4)
        self.tableView_5.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.tableView_5.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0.943, cy:0.505682, angle:0, stop:0 rgba(136, 106, 22, 255), stop:0.113636 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(245, 236, 112, 255), stop:0.505682 rgba(209, 190, 76, 255), stop:0.573864 rgba(187, 156, 51, 255), stop:0.619318 rgba(168, 142, 42, 255), stop:0.681818 rgba(202, 174, 68, 255), stop:0.693182 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.tableView_5.setObjectName("tableView_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 331, 101))
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
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Backup"))
        self.pushButton_3.setText(_translate("Dialog", "Add Contact"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "     Contacts      "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "    Voice Message     "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "      SMS      "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "     MMS    "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "     E-mail    "))
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

