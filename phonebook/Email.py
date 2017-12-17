import smtplib

content = 'Hello Everyone'
mail=smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()
#password = f.open('mail_password.txt')

for line in open('mail_password.txt'):  #put password in a text file and save in same folder
     mail.login('urmailid@gmail.com', line)  #put ur mail id

mail.sendmail('urmailid@gmail.com','sumankanrar25@gmail.com',content) #put ur mail id 

mail.close()
