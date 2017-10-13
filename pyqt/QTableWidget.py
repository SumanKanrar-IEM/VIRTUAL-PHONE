import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)

        self.show()

class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = MyTable(10,10)
        self.setCentralWidget(self.form_widget)

        self.show()

app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())