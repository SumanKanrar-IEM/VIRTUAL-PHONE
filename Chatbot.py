import urllib
import http.cookiejar

cookies = http.cookiejar.CookieJar()
jession_id = ''
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookies))

def login(username, password):

    login_url = 'http://site24.way2sms.com/Login1.action?'
    params ={'username':username,'password':password}
    params=urllib.parse.urlencode(params).encode("utf-8")
    
    headers=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64')]
    opener.addheaders=headers
    try:
        opener.open(login_url, params)
    except IOError:
        pass
    else:
        print("\nLogin Succesful...")

def send_sms(message, receipent):
    
    jession_id = str(cookies).split('~')[1].split(' ')[0]
    
    sms_url = 'http://site24.way2sms.com/smstoss.action?'
    
    sms_data = {'ssaction':'ss','Token':jession_id,'mobile':receipent,'message':message,'msgLen':0}
    
    headers = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    
    sms_data=urllib.parse.urlencode(sms_data).encode("utf-8")
    
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

user=input("Enter your username:  ")
password=input("Enter password:   ")

login(user, password)

number=input("Enter recepient number: ")
message=input("Enter message: ")

send_sms(message, number)




