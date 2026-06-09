from twilio.rest import Client

# Twilio credentials
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! This SMS was sent using Python.",
    from_="+1234567890",   # Your Twilio phone number
    to="+919876543210"     # Recipient phone number
)

print("Message SID:", message.sid)
print("SMS sent successfully!")