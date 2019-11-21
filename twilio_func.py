from decouple import config
from twilio.rest import Client

account_sid = config('TWILIO_ACCOUNT_SID')  # Twilio Account's SID
auth_token = config('TWILIO_AUTH_TOKEN')  # Twilio Account's Auth Token
client = Client(account_sid, auth_token)


def send_rem(date, rem, phone):
	message = client.messages.create(
		from_='whatsapp:+14155238886',
		body='*REMINDER* '+date+'\n'+rem,
		to='whatsapp:+{}'.format(phone)  # Add your WhatsApp No. here
	)
	print(message.sid)