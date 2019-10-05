from decouple import config
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GSheetsHandler:

    def __init__(self):
        self.s = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]

        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            config('GOOGLE_DRIVE_CREDS_JSON_FILE_NAME'), self.s)
        self.client = gspread.authorize(self.creds)

        self.sheet = self.client.open("Whatsapp bot reminders database").sheet1

    def set_data(self, date, msg, sender_phone):
        self.date = date
        self.msg = msg
        self.sender_phone = sender_phone

    def get_write_dimensions(self):
        row_values = self.sheet.row_values(1)
        col_values = self.sheet.col_values(1)
        self.row_filled = len(col_values)
        self.col_filled = len(row_values)
    
    def save_reminder_date(self):
        self.get_write_dimensions()
        self.sheet.update_cell(self.row_filled + 1, 1, self.date)
        self.sheet.update_cell(self.row_filled + 1, 3, self.sender_phone)
        print("saved date!")
        return 0
  
    def save_reminder_body(self):
        self.get_write_dimensions()
        self.sheet.update_cell(self.row_filled, 2, self.msg)
        self.sheet.update_cell(self.row_filled, 3, self.sender_phone)
        print("saved reminder message!")
        return 0

    def get_sheets_data(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            config('GOOGLE_DRIVE_CREDS_JSON_FILE_NAME'), self.s
        )
        client = gspread.authorize(creds)
        worksheet = client.open("Whatsapp bot reminders database").sheet1
        return worksheet.get_all_values()
        