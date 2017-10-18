import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import addcontact_non_exec
class addcontact_class(addcontact_non_exec.Ui_Form, QtWidgets.QWidget):

    def __init__(self):
        super(addcontact_class, self).__init__()
        self.setupUi(self)







        self.btn_set_icon.clicked.connect(self.openFileNameDialog)
        self.btn_save.clicked.connect(self.save_action)




    def save_action(self):
        print("Save button clicked")
        addcontact_obj.hide()
        os._exit(0)
        #os.system('python phonebook_app.py')



    def openFileNameDialog(self):
        print("set icon clicked")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose Contact Icon", "", "Image Files (*.jpg *.png)", options=options)
        if fileName:
            print(fileName)
            pixmap = QtGui.QPixmap(fileName)
            self.contact_icon.setPixmap(pixmap)
            self.contact_icon.setScaledContents(True)





if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    qapp.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    addcontact_obj = addcontact_class()
    addcontact_obj.show()
    qapp.exec_()