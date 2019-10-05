from celery import shared_task
from bot.handlers.gsheets_handler import GSheetsHandler
from bot.handlers.twilio_handler import TwilioHandler


@shared_task
def check_reminders():
	g_sheets_handler = GSheetsHandler()
	twilio_handler = TwilioHandler()

	reminders = g_sheets_handler.get_sheets_data()
	for reminder in reminders:
		date = reminder[0]
		details = reminder[1]
		phone = reminder[2]

		twilio_handler.send_rem(
			date, details, phone
		)

