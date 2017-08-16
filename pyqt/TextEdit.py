import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clr_btn)
        self.clr_btn.clicked.connect(self.clear_text)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()

    def clear_text(self):
        self.text.clear()

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())