from twilio.rest import Client

# Twilio credentials
account_sid = "ADD_YOURS"
auth_token = "ADD_YOURS"
client = Client(account_sid, auth_token)

# Sending SMS
message = client.messages.create(
    body="Hi Nimesh my self you from past few sec!",
    from_="+",
    to="+"
)

print(f"Message sent with SID: {message.sid}")
