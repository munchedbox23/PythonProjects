from datetime import datetime
import requests
import time
import smtplib

MY_LAT = 55.696126
MY_LONG = 37.802254
my_email = "example@gmail.com"
my_password = "your_password"
email_receive = "example@gmail.com"


def is_iss_overhead():
    response = requests.ger(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_letitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_letitude <= MY_LAT and MY_LONG <= iss_longitude<= MY_LONG:
        return True

def is_night():
    parameters = {
        "let":MY_LET,
        "long":MY_LONG,
        "formatted":0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now >=sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(my_email,my_password)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = email_receive,
                msg = f"Subject:LOOK UP\n\nThe ISS is above you in the sky."

            )
