# A window with a button
import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)
    b.setText('Push Me')
    l.setText('Look at Me')
    w.setWindowTitle('PyQt5 Lesson 3')
    b.move(100, 50)
    l.move(110, 100)
    w.setGeometry(100, 100, 300, 200)
    w.show()
    sys.exit(app.exec_())

window()