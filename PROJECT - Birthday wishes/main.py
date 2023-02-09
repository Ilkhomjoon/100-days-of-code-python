from datetime import datetime
import pandas
from random import randint
import smtplib

MY_EMAIL = ""
PASSWORD = ""

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        letter = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        global birthday_person
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday\n\n{letter}")
