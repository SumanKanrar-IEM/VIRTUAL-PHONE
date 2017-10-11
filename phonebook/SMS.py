from twilio.rest import Client

#account sid and auth token from twilio account

account_sid = "AC4e9647745ad74b4b505ae89084eda74b"
auth_token = "f8c22ad19cb744fd5b36e835c983211d"
client = Client(account_sid, auth_token)


message = client.messages.create(body="Hello Everybody!!!",to="+918013120648",from_="+19124175695")
#text message
print message.sid
