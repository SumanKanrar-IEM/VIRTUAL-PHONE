        ##########################################################
        #                       BROWSER                          #
        #                         BY                             #
        #                   SUMAN  KANRAR                        #
        ##########################################################


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import sys
import os

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        self.show()
        self.setWindowTitle("Browser")
        self.setWindowIcon(QIcon('browser_icon.png'))
        self.setGeometry(50,50,1200,800)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.setCentralWidget(self.browser)

        navtab = QToolBar("Navigation")
        navtab.setIconSize(QSize(20,20))
        self.addToolBar(navtab)

        back_btn = QAction(QIcon("nav_back.png"), "Back", self)
        back_btn.setStatusTip("Back to the Previous Page")
        back_btn.setShortcut("Ctrl+z")
        back_btn.triggered.connect(self.browser.back)
        navtab.addAction(back_btn)


        next_btn = QAction(QIcon('nav_forward.png'), "Forward", self)
        next_btn.setStatusTip("Forward to the next page")
        next_btn.setShortcut("Ctrl+x")
        next_btn.triggered.connect(self.browser.forward)
        navtab.addAction(next_btn)

        reload_btn = QAction(QIcon('reload.png'), "Reload", self)
        reload_btn.setStatusTip("Reload")
        reload_btn.setShortcut("Ctrl+r")
        reload_btn.triggered.connect(self.browser.reload)
        navtab.addAction(reload_btn)

        navtab.addSeparator()

        home_btn = QAction(QIcon('home.png'), "Home", self)
        home_btn.setStatusTip("Home")
        home_btn.triggered.connect(self.navigate_home)
        navtab.addAction(home_btn)

        navtab.addSeparator()

        self.httpsicon = QLabel()
        self.httpsicon.resize(5,5)
        self.httpsicon.setPixmap(QPixmap('https.png'))
        self.httpsicon.setScaledContents(True)
        #self.httpsicon.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        navtab.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtab.addWidget(self.urlbar)
        self.browser.urlChanged.connect(self.update_urlbar)

        #self.menuBar().setNativeMenuBar(False)

        #file_menu = self.menuBar().addMenu("&File")

##########################################################################################################
        #open_file_action = QAction(QIcon("open.png"), "Open File", self)
        #open_file_action.setStatusTip("Open from File")
        #open_file_action.triggered.connect(self.open_file)
        #file_menu.addAction(open_file_action)

        #save_file_action = QAction(QIcon("save.png"), "Save Page As", self)
        #save_file_action.setStatusTip("Save current page to file")
        #save_file_action.triggered.connect(self.save_file)
        #file_menu.addAction(save_file_action)


        #print_action = QAction(QIcon("print.png"), "Print", self)
        #print_action.setStatusTip("Print Page")
        #print_action.setShortcut("Ctrl+p")
        #print_action.triggered.connect(self.print_page)
        #file_menu.addAction(print_action)

##############################################################################################################
        navtab.addSeparator()

        stop_btn = QAction(QIcon('cancel.png'), "Stop", self)
        stop_btn.setStatusTip("Stop loading the current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtab.addAction(stop_btn)


    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        #print(q.scheme())
        if q.scheme()=="":
            q.setScheme("http")

        self.browser.setUrl(q)

############################################################################################3
    #def print_page(self):
        #print("Printing!!")
        #dlg = QPrintPreviewDialog()
        #dlg.paintRequested.triggered(self.browser.print_)
        #dlg.exec_()


    #def open_file(self):
        #filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Hypertext Markup Language (*.htm *.html);;""All files(*.*)")
        #if filename:
            #with open(filename, 'r') as f:
              #  html = f.read()

            #self.browser.setHtml(html)
            #self.urlbar.setText(filename)


    #def save_file(self):
        #filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "", "Hypertext Markup Language (*.htm *.html);;""All files(*.*)")

#        if filename:
 #           html = self.browser.page().mainFrame().toHtml()
  #          with open(filename, 'w') as f:
   #             f.write(html)
########################################################################################################

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))


    def update_urlbar(self, q):

        if(q.scheme()=='https'):
            #Secure lock icon
            self.httpsicon.setPixmap(QPixmap('https.png'))

        else:
            self.httpsicon.setPixmap(QPixmap('http.png'))
            #Unsecure lock icon


        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)




app = QApplication(sys.argv)
app.setApplicationName("Blazing Browser")
app.setStyle(QStyleFactory.create('Fusion'))
#app.setOrganizationName("CLASHERS")
#app.setOrganizationDomain("https://about.me/suman.kanrar")
window = MainWindow()
window.show()
app.exec_()
