from twilio.rest import Client

# 🔐 Use your actual credentials from https://www.twilio.com/console
account_sid = 'id'
auth_token = 'access token'

client = Client(account_sid, auth_token)

# ✅ Twilio sandbox number (don’t change)
from_whatsapp_number = 'whatsapp:+14000000000'

# ✅ Your WhatsApp number that joined sandbox
to_whatsapp_number = 'whatsapp:+91700000000'

# ✅ Message to send
message = client.messages.create(
    body='What are you doing?',
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(f"✅ Message sent! SID: {message.sid}")
