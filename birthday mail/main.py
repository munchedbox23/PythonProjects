import pandas
import datetime as dt
import smtplib
from random import randint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

email_send = "Munchedbox230@yandex.ru"
password = "ravekipygogedixz"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv", encoding="utf-8")
birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birtday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path, "r", encoding="utf-8") as letter_data:
        contents = letter_data.read()
        contents = contents.replace("[NAME]",birtday_person["name"])

    # create message object
    message = MIMEMultipart()
    message["Subject"] = Header("С Днем Рождения!", "utf-8")
    message["From"] = email_send
    message["To"] = birtday_person["email"]

    # attach message body
    body = MIMEText(contents, "plain", "utf-8")
    message.attach(body)

    # create SMTP session and send email
    with smtplib.SMTP("smtp.yandex.ru",587) as connection:
        connection.starttls()
        connection.login(email_send,password)
        connection.sendmail(
            from_addr = email_send,
            to_addrs = birtday_person["email"],
            msg = message.as_string()
        )
