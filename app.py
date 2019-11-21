from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import (
    save_reminder_date,
    save_reminder_body
)

from dateutil.parser import parse

app = Flask(__name__)
count = 0

@app.route("/sms", methods=['POST'])
def reply():
    sender = request.form['From']
    sender_phone = sender.split('whatsapp:')[1]
    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    print(incoming_msg)
    message = response.message()
    responded = False
    words = incoming_msg.split('@')
    if "hello" in incoming_msg:
        reply = "Hello! \nDo you want to set a reminder?"
        message.body(reply)
        responded = True

    if len(words) == 1 and "yes" in incoming_msg:
        reminder_string = "Please provide date in the following "\
            "format only.\n\n"\
            "*Date @* _type the date_ "
        message.body(reminder_string)
        responded = True
    if len(words) == 1 and "no" in incoming_msg:
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
            set_reminder_date(input_string, sender_phone)
            message.body(reply)
            responded = True
        if input_type == "reminder":
            print("yuhu")
            reply = "Your reminder is set!"
            set_reminder_body(input_string, sender_phone)
            message.body(reply)
            responded = True
        
    if not responded:
        print("why", input_type)
        message.body(
            'Incorrect request format. Please enter in the correct format'
        )
    
    return str(response)

    
def set_reminder_date(msg, sender_phone):
    p = parse(msg)
    date = p.strftime('%m/%d/%Y')
    save_reminder_date(date, sender_phone)
    return 0

    
def set_reminder_body(msg, sender_phone):
    save_reminder_body(msg, sender_phone)
    return 0


if __name__ == "__main__":
    app.run(debug=True, port=5001,)