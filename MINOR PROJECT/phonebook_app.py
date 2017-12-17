import sys
import os
from twilio.rest import Client
import smtplib
import urllib
import requests
import http.cookiejar
from PyQt5 import QtCore, QtGui, QtWidgets
import phonebook_non_exec
import addcontact_app
from addcontact_app import addcontact_class
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QTableWidget, QMessageBox
import csv




class Phonebook_class(phonebook_non_exec.Ui_Dialog, QtWidgets.QDialog):

    audios_list = []

    def __init__(self):
        super(Phonebook_class, self).__init__()
        self.setupUi(self)



        self.table_contacts.setHorizontalHeaderLabels(['Name','Phone No.','Email ID','Address','DOB'])
        self.table_contacts.resizeColumnsToContents()
        self.table_contacts.horizontalHeader().setDefaultSectionSize(150)
        self.table_contacts.verticalHeader().setVisible(False)
        self.table_contacts.horizontalHeader().setFixedHeight(45)
        self.table_contacts.horizontalHeader().setStyleSheet("font: 75 13pt \"Comic Sans MS\";\n")

        if self.tabWidget.currentWidget() == self.tab_contacts:
            print("Contacts tab is active by default")
            self.open_sheet()

        self.audios_list = ['Congratulations','Good Morning','Good Night','Happy Birthday','Merry Christmas','Thank You']
        self.list_vmsg_audios.addItems(self.audios_list)
        self.list_vmsg_audios.setDisabled(True)


        self.sms_area.setDisabled(True)

        self.mailID_area.setDisabled(True)
        self.mail_area.setDisabled(True)



        self.list_vmsg_contacts.itemClicked.connect(self.list_contacts_selected)
        self.list_vmsg_audios.itemClicked.connect(self.list_audio_selected)
        self.list_sms_contacts.itemClicked.connect(self.list_SMSrecipient_selected)
        self.list_email_contacts.itemClicked.connect(self.list_EMAILrecipient_selected)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.btn_add_contact.clicked.connect(self.addContact)
        self.btn_backup.clicked.connect(self.Backup_Contacts)
        self.btn_send_vmsg.clicked.connect(self.send_voicemsg)
        self.btn_send_sms.clicked.connect(self.send_sms)
        self.btn_send_email.clicked.connect(self.send_mail)




    def tab_changed(self):


        if self.tabWidget.currentWidget() == self.tab_contacts:
            print("contacts tab is active")
            self.open_sheet()


        if self.tabWidget.currentWidget() == self.tab_voicemsg:
            print("voice message tab is active")
            self.open_voicelist()


        if self.tabWidget.currentWidget() == self.tab_sms:
            print("sms tab is active")
            self.open_smslist()

        if self.tabWidget.currentWidget() == self.tab_email:
            print("Email tab is active")
            self.open_maillist()




    def send_voicemsg(self):

        vmsg_recipient = "+91" + str(self.phonenumber)
        print(vmsg_recipient)

        '''Provide proper account details from twilio.com after creating an account'''

        # alternate account_sid = "Ccbd1807fccb261db8b7d18f0983b412b"
        # alternate auth-token = "da34ba8de62e3d7fa45fc7f92926e15"
        # alternate phone number = "+3203320575"

        client = Client(account_sid, auth_token)

        call = client.calls.create(to= vmsg_recipient, from_="+1914175695", url= self.URL)
        print(call.sid)
        self.list_vmsg_audios.setDisabled(True)



    def send_sms(self):

        cookies = http.cookiejar.CookieJar()
        jession_id = ''
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookies))

        message = self.sms_area.toPlainText()
        recipient = self.recipient_number
        print(recipient)
        usr = #give your way2sms username
        password = #Give the respective password

        login_url = 'http://site24.way2sms.com/Login1.action?'
        params = {'username': usr, 'password': password}
        params = urllib.parse.urlencode(params).encode("utf-8")

        headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64')]
        opener.addheaders = headers
        try:
            opener.open(login_url, params)
        except IOError:
            pass
        else:
            print("\nLogin Succesful...")

        jession_id = str(cookies).split('~')[1].split(' ')[0]

        sms_url = 'http://site24.way2sms.com/smstoss.action?'

        sms_data = {'ssaction': 'ss', 'Token': jession_id, 'mobile': recipient, 'message': message, 'msgLen': 0}

        headers = [('Referer', 'http://site25.way2sms.com/sendSMS?Token=' + jession_id)]

        sms_data = urllib.parse.urlencode(sms_data).encode("utf-8")

        opener.addheaders = headers
        try:
            sms_page = opener.open(sms_url, sms_data)
        except IOError:
            pass
        else:
            if b'Message has been submitted successfully' in sms_page.read():
                print('Message has been submitted successfully')
            else:
                print('Sms Sending Failed')




        self.sms_area.clear()
        self.sms_area.setDisabled(True)





    def send_mail(self):
        print("Send Email button clicked")

        content = self.mail_area.toPlainText()
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()
        # password = f.open('mail_password.txt')

        for line in open('mail_password.txt'):  #put the password in a text file in the same folder
            mail.login('urmailid@gmail.com', line) #put your owm mail id 

        mail.sendmail('urmailid@gmail.com', self.mail_id, content)

        mail.close()

        print("Successfully sent")
        self.mail_area.clear()
        self.mailID_area.clear()


    def list_contacts_selected(self):
        self.list_vmsg_contacts.setEnabled(True)
        self.list_vmsg_contacts.currentItem().setSelected(True)


        a = self.list_vmsg_contacts.currentItem().text()


        self.selected_row = self.list_vmsg_contacts.currentRow()
        self.phonenumber = self.table_contacts.item(self.selected_row, 1).text()
        self.list_vmsg_audios.setDisabled(False)


        print(a, self.selected_row)
        print(self.phonenumber)




    def list_audio_selected(self):
        audioSelected = self.list_vmsg_audios.currentItem().text()
        row_audioSelected = self.list_vmsg_audios.currentRow()

        if row_audioSelected == 0:
            self.URL = "https://sumankanrar25.000webhostapp.com/upload/congratulations.mp3"
        elif row_audioSelected == 1:
            self.URL = "https://sumankanrar25.000webhostapp.com/upload/good%20morning.mp3"
        elif row_audioSelected == 2:
            self.URL = "https://sumankanrar25.000webhostapp.com/upload/good%20night.mp3"
        elif row_audioSelected == 3:
            self.URL = "https://sumankanrar25.000webhostapp.com/upload/happy%20birthday.mp3"
        elif row_audioSelected == 4:
            self.URL = "https://sumankanrar25.000webhostapp.com/upload/Merry%20christmas.mp3"
        else:
            self.URL = "https://sumankanrar25.000webhostapp.com/upload/thank%20you.mp3"

        print(audioSelected, row_audioSelected)





    def list_SMSrecipient_selected(self):
        print("Selected a recipient for sms")
        self.list_sms_contacts.setEnabled(True)
        self.list_sms_contacts.currentItem().setSelected(True)

        self.selected_recipient = self.list_sms_contacts.currentRow()
        self.recipient_number = self.table_contacts.item(self.selected_recipient, 1).text()

        print(self.selected_recipient, self.recipient_number)
        self.sms_area.setDisabled(False)




    def list_EMAILrecipient_selected(self):
        print("Selected the mail id for email")
        self.list_email_contacts.setEnabled(True)
        self.list_email_contacts.currentItem().setSelected(True)

        self.selected_mailrecipient = self.list_email_contacts.currentRow()
        self.mail_id = self.table_contacts.item(self.selected_mailrecipient, 2).text()

        print(self.selected_mailrecipient, self.mail_id)
        self.mailID_area.setDisabled(False)
        self.mail_area.setDisabled(False)

        self.mailID_area.setText("To :           " + self.mail_id)




    def open_sheet(self):
        #self.check_change = False
        path = ('./contacts.csv', 'CSV(*.csv)')
        print(path)
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.table_contacts.setRowCount(0)
                self.table_contacts.setColumnCount(5)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.table_contacts.rowCount()
                    self.table_contacts.insertRow(row)
                    if len(row_data) > 10:
                        self.table_contacts.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.table_contacts.setItem(row, column, item)
        #self.check_change = True
        print(self.table_contacts.rowCount())




    def addContact(self):
        print("add contact clicked")
        QtCore.QCoreApplication.processEvents()
        os.system('python addcontact_app.py')
        # self.window = QtWidgets.QDialog()
        # self.ui = addcontact_class()
        # self.ui.setupUi(self.window)
        # self.window.show()
        #phonebook_obj.hide()




    def Backup_Contacts(self):

        print("backup button clicked")
        path = QFileDialog.getSaveFileName(self, 'Backup Contacts', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w', newline='') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.table_contacts.rowCount()):
                    row_data = []
                    for column in range(self.table_contacts.columnCount()):
                        item = self.table_contacts.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)


        print("all operations successful")





    def open_voicelist(self):
        print("Entered function")
        self.list_vmsg_contacts.clear()
        for vmsgCon_row in range(self.table_contacts.rowCount()):
            self.list_vmsg_contacts.addItem(self.table_contacts.item(vmsgCon_row, 0).text())




    def open_smslist(self):
        print("Entered function")
        self.list_sms_contacts.clear()
        for smsCon_row in range(self.table_contacts.rowCount()):
            self.list_sms_contacts.addItem(self.table_contacts.item(smsCon_row, 0).text())




    def open_maillist(self):
        print("Entered function")
        self.list_email_contacts.clear()
        for emailCon_row in range(self.table_contacts.rowCount()):
            self.list_email_contacts.addItem(self.table_contacts.item(emailCon_row, 0).text())






if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    qapp.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    phonebook_obj = Phonebook_class()
    phonebook_obj.show()
    qapp.exec_()
