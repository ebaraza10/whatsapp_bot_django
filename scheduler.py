from decouple import config
from twilio_func import *
from datetime import datetime
from datetime import date
from datetime import time
import apscheduler
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dateutil.parser import parse

s = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

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


scheduler = BlockingScheduler()
creds = ServiceAccountCredentials.from_json_keyfile_name(
    config('GOOGLE_DRIVE_CREDS_JSON_FILE_NAME'), s
)
client = gspread.authorize(creds)


worksheet = client.open("Whatsapp bot reminders database").sheet1
list_of_lists = worksheet.get_all_values()
print(list_of_lists)
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
            scheduler.add_job(
                send_rem, 'date', run_date=utc_dt,
                args=[row[0], row[1], row[2]]
            )
        else:
            pass
    i += 1
        
scheduler.start()