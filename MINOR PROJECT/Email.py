import smtplib

content = 'Hello Everyone'
mail=smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()
#password = f.open('mail_password.txt')

for line in open('mail_password.txt'):
     mail.login('sumankanrar420@gmail.com', line)

mail.sendmail('sumankanrar420@gmail.com','sumankanrar25@gmail.com',content)

mail.close()
