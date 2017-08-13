import smtplib

content = 'Hello Everyone'
mail=smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('sumankanrar420@gmail.com','sumanpassword')

mail.sendmail('sumankanrar420@gmail.com','sumankanrar25@gmail.com',content)

mail.close()
