import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFontDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 font dialog - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Open PyQt5 Font Dialog', self)
        button.setToolTip('font dialog')
        button.move(50,50)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        openFontDialog(self)


def openFontDialog(self):
    font, ok = QFontDialog.getFont()
    if ok:
        print(font.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
