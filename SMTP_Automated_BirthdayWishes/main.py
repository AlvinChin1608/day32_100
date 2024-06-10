import datetime as dt
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "alvin@gmail.com"
PASSWORD = "" # generate the "App Password" in google security password

# 2. Check if today matches a birthday in the birthdays.csv
# Only the month and day matter.
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Create a dictionary from birthdays.csv
data = pd.read_csv("birthdays.csv")

# Dictionary comprehension template for pandas DataFrame
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Compare and see if today's month/day matches one of the keys in birthday_dict
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    # Create the email message
    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = f"Today is {birthday_person['name']}'s birthday"
    msg["From"] = MY_EMAIL
    msg["To"] = birthday_person["email"]

    # Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=msg.as_string())

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
