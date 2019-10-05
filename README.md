# A Whatsapp bot in django

## Functionality supported:
Allow users to set reminders with dates and reminder messages via Whatsapp
Automatically sends set reminders on the chosen date via Whatsapp

## Technologies used:
* Python(Flask)
* Google sheets(storage of reminders/database)
* Docker
* Celery
* Redis


## How to setup:
1. Setup and enable Google sheets API. 
2. Rename .env_template to .env
3. Edit .env variables to match your environement
4. Run docker-compose -f docker-compose.yml up -d