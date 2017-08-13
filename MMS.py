from twilio.rest import Client

#account sid and auth token from twilio account

account_sid = "AC4e9647745ad74b4b505ae89084eda74b"
auth_token = "f8c22ad19cb744fd5b36e835c983211d"
client = Client(account_sid, auth_token)

message2 = client.messages.create(to="+918013120648",from_="+19124175695",body="Hello there!",media_url=['https://scontent.fccu5-1.fna.fbcdn.net/v/t1.0-9/19429811_879418028878600_7909594136451512265_n.jpg?oh=10209c3a2703c33a6e702628b5d048d9&oe=59D72774'])#,'https://drive.google.com/open?id=0B58T0x3Ngp38QkN1TjlmY2Q3MDA'])
#message2 is MMS
print message2.sid
