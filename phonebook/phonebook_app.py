import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import phonebook_non_exec
import addcontact_app
from addcontact_app import addcontact_class
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QTableWidget, QMessageBox
import csv
class Phonebook_class(phonebook_non_exec.Ui_Dialog, QtWidgets.QDialog):

    def __init__(self):
        super(Phonebook_class, self).__init__()
        self.setupUi(self)

        self.table_contacts.setHorizontalHeaderLabels(['Name','Phone No.','Email ID','Address','DOB'])
        self.table_contacts.resizeColumnsToContents()
        self.table_contacts.horizontalHeader().setDefaultSectionSize(150)
        self.table_contacts.verticalHeader().setVisible(False)
        self.table_contacts.horizontalHeader().setFixedHeight(45)
        self.table_contacts.horizontalHeader().setStyleSheet("font: 75 13pt \"Comic Sans MS\";\n")

        if self.tabWidget.currentWidget() == self.tab_contacts:
            print("Contacts tab is active by default")
            self.open_sheet()

        self.tabWidget.currentChanged.connect(self.tab_changed)






        self.btn_add_contact.clicked.connect(self.addContact)
        self.btn_backup.clicked.connect(self.Backup_Contacts)


    def tab_changed(self):


        if self.tabWidget.currentWidget() == self.tab_contacts:
            print("contacts tab is active")

        if self.tabWidget.currentWidget() == self.tab_voicemsg:
            print("voice message tab is active")

        if self.tabWidget.currentWidget() == self.tab_sms:
            print("sms tab is active")

        if self.tabWidget.currentWidget() == self.tab_email:
            print("Email tab is active")



    def open_sheet(self):
        #self.check_change = False
        path = ('./contacts.csv', 'CSV(*.csv)')
        # QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        print(path)
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.table_contacts.setRowCount(0)
                self.table_contacts.setColumnCount(5)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.table_contacts.rowCount()
                    self.table_contacts.insertRow(row)
                    if len(row_data) > 10:
                        self.table_contacts.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.table_contacts.setItem(row, column, item)
        #self.check_change = True

    def addContact(self):
        print("add contact clicked")
        os.system('python addcontact_app.py')
        # self.window = QtWidgets.QDialog()
        # self.ui = addcontact_class()
        # self.ui.setupUi(self.window)
        # self.window.show()
        #phonebook_obj.hide()




    def Backup_Contacts(self):

        print("backup button clicked")
        path = QFileDialog.getSaveFileName(self, 'Backup Contacts', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.table_contacts.rowCount()):
                    row_data = []
                    for column in range(self.table_contacts.columnCount()):
                        item = self.table_contacts.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)


        print("all operations successful")





if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    qapp.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    phonebook_obj = Phonebook_class()
    phonebook_obj.show()
    qapp.exec_()
