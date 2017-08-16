#saving text files as .txt files

import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Save')

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clr_btn)
        self.clr_btn.clicked.connect(self.save_text)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()

    def save_text(self):
        with open('Saving_text_files.txt', 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())