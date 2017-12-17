from twilio.rest import Client

#account sid and auth token from twilio account

account_sid = "xxxxxxxx5ad74b4b505ae89084eda74b"
auth_token = "xxxxxxxxxx744fd5b36e835c983211d"
client = Client(account_sid, auth_token)


message = client.messages.create(body="Hello Everybody!!!",to="+xxxxxx20648",from_="+xxxxx5695")  #to: sender phone number
#text message
print message.sid
