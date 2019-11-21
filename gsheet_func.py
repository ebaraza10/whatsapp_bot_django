from decouple import config
import gspread
from oauth2client.service_account import ServiceAccountCredentials

s = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    config('GOOGLE_DRIVE_CREDS_JSON_FILE_NAME'), s)
client = gspread.authorize(creds)

sheet = client.open("Whatsapp bot reminders database").sheet1
row_values = sheet.row_values(1)
col_values = sheet.col_values(1)
row_filled = len(col_values)
col_filled = len(row_values)

    
def save_reminder_date(date, sender_phone):
    sheet.update_cell(row_filled + 1, 1, date)
    sheet.update_cell(row_filled + 1, 3, sender_phone)
    print("saved date!")
    return 0

   
def save_reminder_body(msg, sender_phone):
    sheet.update_cell(row_filled + 1, 2, msg)
    sheet.update_cell(row_filled + 1, 3, sender_phone)
    print("saved reminder message!")
    return 0