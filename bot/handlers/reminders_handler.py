from datetime import datetime
from datetime import date
from dateutil.parser import parse
import pytz
from .gsheets_handler import GSheetsHandler
from .twilio_handler import TwilioHandler


class RemindersHandler:

	def __init__(self, request_data):
		self.request_data = request_data
		self.gsheets_handler = GSheetsHandler()
		self.twilio_handler = TwilioHandler()
		self.set_twilio_data()

	def set_twilio_data(self):
		sender = self.request_data['From']
		self.sender_phone = sender.split('whatsapp:')[1]
		self.incoming_msg = self.request_data['Body'].lower()
		# self.set_user_request_data()

	def set_user_request_data(self):
		self.sender_phone = self.request_data['sender_phone']
		self.date = self.request_data['date']
		self.details = self.request_data['details']

	def get_response(self):
		response = self.twilio_handler.MessagingResponse()
		print(self.incoming_msg)
		message = response.message()
		responded = False
		words = self.incoming_msg.split('@')
		if "hello" in self.incoming_msg:
			reply = "Hello! \nDo you want to set a reminder?"
			message.body(reply)
			responded = True

		if len(words) == 1 and "yes" in self.incoming_msg:
			reminder_string = "Please provide date in the following "\
				"format only.\n\n"\
				"*Date @* _type the date_ "
			message.body(reminder_string)
			responded = True
		if len(words) == 1 and "no" in self.incoming_msg:
			reply = "Ok. Have a nice day!"
			message.body(reply)
			responded = True

		elif len(words) != 1:
			input_type = words[0].strip().lower()
			input_string = words[1].strip()
			if input_type == "date":
				reply = "Please enter the reminder message in the following"\
					"format only.\n\n"\
					"*Reminder @* _type the message_"
				self.gsheets_handler.set_data(input_string, '', self.sender_phone)
				self.gsheets_handler.save_reminder_date()  # input_string, self.sender_phone)
				message.body(reply)
				responded = True
			if input_type == "reminder":
				print("yuhu")
				reply = "Your reminder is set!"
				self.gsheets_handler.set_data('', input_string, self.sender_phone)
				self.gsheets_handler.save_reminder_body()  # input_string, self.sender_phone)
				message.body(reply)
				responded = True

		if not responded:
			print("why", input_type)
			message.body(
				'Incorrect request format. Please enter in the correct format'
			)

		return str(response)

	def get_reminders(self):
		dt = date.today().strftime('%d/%m/%Y')
		now_date = datetime.strptime(dt, '%d/%m/%Y')
		rem_day = now_date.day
		rem_month = now_date.month
		rem_year = now_date.year

		t = datetime(rem_year, rem_month, rem_day, 22, 23)
		# local = pytz.timezone("Asia/Kolkata")
		local = pytz.timezone("Africa/Nairobi")
		local_dt = local.localize(t, is_dst=None)
		utc_dt = local_dt.astimezone(pytz.utc)

		list_of_lists = self.gsheets_handler.get_sheets_data()
		print(list_of_lists)

		reminders_list = []
		i = 0
		for row in list_of_lists:
			# print(row[2])
			if i != 0:
				p = parse(row[0])
				print(p)
				pp = p.strftime('%d/%m/%Y')
				print(pp)
				print(dt)
				print(row[1])
				if pp == dt:
					reminders_list.append(
						{'date': row[0], 'rem': row[1], 'phone': row[2]}
					)
						
				else:
					pass
			i += 1



