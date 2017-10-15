import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import phonebook_non_exec
class Phonebook_class(phonebook_non_exec.Ui_Dialog, QtWidgets.QDialog):

    def __init__(self):
        super(Phonebook_class, self).__init__()
        self.setupUi(self)








if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    phonebook_obj = Phonebook_class()
    phonebook_obj.show()
    qapp.exec_()
