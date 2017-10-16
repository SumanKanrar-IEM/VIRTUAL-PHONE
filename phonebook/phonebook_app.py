import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import phonebook_non_exec
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










if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    qapp.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    phonebook_obj = Phonebook_class()
    phonebook_obj.show()
    qapp.exec_()
