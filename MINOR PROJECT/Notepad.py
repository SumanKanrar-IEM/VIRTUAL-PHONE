import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QFontDialog, QStyleFactory
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp
from PyQt5.QtGui import QFont, QIcon


class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')
        #self.font_btn = QPushButton('Change Font')
        # self.clr_btn.setStyle(QStyleFactory.create('Fusion'))
        # self.sav_btn.setStyle(QStyleFactory.create('Windows'))
        # self.opn_btn.setStyle(QStyleFactory.create('Cleanlooks'))

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.sav_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        #self.setWindowTitle("notepad")
        #self.setWindowIcon(QIcon('notepad.png'))



        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()


class Writer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        font_action = QAction('&Font', self)

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)
        edit.addAction(font_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)
        font_action.triggered.connect(self.font_changer1)
        self.setWindowTitle("Notepad")
        self.setWindowIcon(QIcon('pnotepad.png'))
        self.show()

    def quit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == 'New':
            self.form_widget.clear_text()
        elif signal == '&Open':
            self.form_widget.open_text()
        elif signal == '&Save':
            self.form_widget.save_text()


    def font_changer1(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.form_widget.text.setFont(font)




app = QApplication(sys.argv)
app.setStyle(QStyleFactory.create('Fusion'))
writer = Writer()
sys.exit(app.exec_())
