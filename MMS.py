from twilio.rest import Client

#account sid and auth token from twilio account

account_sid = "AC4e9647745ad74b4b505ae89084eda74b"
auth_token = "f8c22ad19cb744fd5b36e835c983211d"
client = Client(account_sid, auth_token)

message2 = client.messages.create(to="+919163149163",from_="+19124175695",body="Hello there!",media_url=['https://sumankanrar25.000webhostapp.com/upload/pic.jpg'])#,'https://drive.google.com/open?id=0B58T0x3Ngp38QkN1TjlmY2Q3MDA'])
#message2 is MMS
print (message2.sid)
