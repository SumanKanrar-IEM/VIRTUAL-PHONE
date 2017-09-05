from twilio.rest import Client

#account sid and auth token from twilio account

account_sid = "AC4e9647745ad74b4b505ae89084eda74b"
auth_token = "f8c22ad19cb744fd5b36e835c983211d"
client = Client(account_sid, auth_token)

message = client.messages.create(body="Hey Surbhi! Batman here",to="+919163149163",from_="+19124175695")   #text message
message2 = client.messages.create(to="+919163149163",from_="+19124175695",body="Hello there!",media_url=['https://scontent.fccu5-1.fna.fbcdn.net/v/t1.0-9/19429811_879418028878600_7909594136451512265_n.jpg?oh=10209c3a2703c33a6e702628b5d048d9&oe=59D72774'])#,'https://drive.google.com/open?id=0B58T0x3Ngp38QkN1TjlmY2Q3MDA'])
#message2 is MMS
call = client.calls.create(to="+919330286302",from_="+19124175695",url="https://sumankanrar25.000webhostapp.com/upload/voice.mp3")
                           #"https://sites.google.com/site/infotricks1on1/home/SampleAudio_0.5mb.mp3?attredirects=0&d=1.mp3")
#call for voice call outgoing

#print (message.sid)
#print (message2.sid)
print(call.sid)


#verified on jio,airtel,vodafone
