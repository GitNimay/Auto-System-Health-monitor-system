from twilio.rest import Client

# Twilio credentials
account_sid = "AC05f752a99c3de6996e956c2474a9d9ca"
auth_token = "6e2a543f16c3be18628c33cb600c03bb"
client = Client(account_sid, auth_token)

# Sending SMS
message = client.messages.create(
    body="Hi Nimesh my self you from past few sec!",
    from_="+18304944676",
    to="+918767401706"
)

print(f"Message sent with SID: {message.sid}")
