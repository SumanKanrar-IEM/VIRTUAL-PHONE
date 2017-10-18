import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import phonebook_non_exec
import addcontact_app
from addcontact_app import addcontact_class
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










        self.btn_add_contact.clicked.connect(self.addContact)
        self.btn_backup.clicked.connect(self.Backup_Contacts)



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







if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    qapp.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    phonebook_obj = Phonebook_class()
    phonebook_obj.show()
    qapp.exec_()
