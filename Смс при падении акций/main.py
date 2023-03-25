STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "5FOI69GMQDIQ4B69"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "a1fb36ee33124a849cfe6629eee3e9d8"
email_send = "artem.pobortsew@gmail.com"
password = "vrrdsmbffldghdnt"

import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

stock_parametres = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":STOCK_NAME,
    "interval":"5min",
    "apikey":STOCK_API
}

response = requests.get(url = STOCK_ENDPOINT, params = stock_parametres)
response.raise_for_status()
data = response.json()["Time Series (5min)"]
data_list = [value for (key,value) in data.items()]
yesterda_closing_data =data_list[0]["4. close"]
before_yesterday_closing_data = data_list[1]["4. close"]
difference = abs(float(yesterda_closing_data) - float(before_yesterday_closing_data))

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference) / float(yesterda_closing_data) * 100)

if abs(diff_percent) > -1:
    news_params = {
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME
    }

    news_response =requests.get(NEWS_ENDPOINT, params = news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        message = MIMEMultipart()
        message["Subject"] = Header("article", "utf-8")
        message["From"] = email_send
        message["To"] = "rubcov_egorka@mail.ru"

    # attach message body
        body = MIMEText(article, "plain", "utf-8")
        message.attach(body)

        # create SMTP session and send email
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(email_send,password)
            connection.sendmail(
                from_addr = email_send,
                to_addrs = "rubcov_egorka@mail.ru",
                msg = message.as_string()
            )
