from random import randint
import pandas 
import datetime as dt
import smtplib

email_send = "Egor032324@mail.ru"
password = "mDzb7pNeKaC1JWwzDRXd"
today = dt.datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("Birthday wisher/birthdays.csv")
birthay_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthay_dict:
    birthday_person = birthay_dict[today_tuple]
    file_path = f"Birthday wisher/letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
    
    with smtplib.SMTP("smtp.mail.ru",587) as connection:
        connection.starttls()
        connection.login(email_send,password)
        connection.sendmail(
            from_addr= email_send,
            to_addrs=birthday_person["email"],
            msg = f"Subject:Happy Birthday!\n\n{contents}"
        
