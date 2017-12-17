from twilio.rest import Client

#account sid and auth token from twilio account

account_sid = "xxxxxad74b4b505ae89084eda74b"
auth_token = "xxxxxxxxxxxx36e835c983211d"


client = Client(account_sid, auth_token)

call = client.calls.create(to="+91xxxxx63",from_="+1xxxxx695",url="https://sites.google.com/site/infotricks1on1/home/SampleAudio_0.5mb.mp3?attredirects=0&d=1.mp3")
#to: sender phone number  from:  own twilio number                          
#call for voice call outgoing

#print (message.sid)
#print (message2.sid)
print(call.sid)


#verified on jio,airtel,vodafone
