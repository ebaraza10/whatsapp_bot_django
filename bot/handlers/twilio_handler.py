from decouple import config
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


class TwilioHandler:

	def __init__(self):
		self.account_sid = config('TWILIO_ACCOUNT_SID')  # Twilio Account's SID
		self.auth_token = config('TWILIO_AUTH_TOKEN')  # Twilio Account's Auth Token
		self.client = Client(self.account_sid, self.auth_token)
		self.MessagingResponse = MessagingResponse

	def send_rem(self, date, rem, phone):
		message = self.client.messages.create(
			from_='whatsapp:+14155238886',
			body='*REMINDER* '+date+'\n'+rem,
			to='whatsapp:+{}'.format(phone)  # Add your WhatsApp No. here
		)
		print(message.sid)
