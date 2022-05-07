""""
this can be edited to real trading signal notification
use real-time websocket from polygon.io
put in buy price
set notification when current price is higher then buyprice by e.g. 0.1 percent
Think about this...
"""

import requests
from datetime import date, timedelta
from twilio.rest import Client

stockapi = "1ETRf5UQsNi8jcBoAZ6WNhiy63xtlOTc"
newsapi = "9d176b3cc91b4538bd0d42d84d7f9843"

smsauth = "AC247b389d3f175e00be3e5f1ed45739b8"
smstoken = "f6dfd28cc64dfde2859a772c5a5a009a"
smsfrom = "+17135973138"
smsto = "+19292490726"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY = date.today()
days = [TODAY - timedelta(days = 2), TODAY - timedelta(days = 1)]



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stockparams = {
    "apiKey": stockapi
}

prices = []
if 1 < TODAY.weekday() < 6:
    for d in days:
        response = requests.get(f"https://api.polygon.io/v1/open-close/{STOCK}/{d}", params=stockparams)
        response.raise_for_status()
        stockdata = response.json()
        prices.append([stockdata['open'], stockdata['close']])

percentage = (prices[1][0] - prices[0][1]) / prices[0][1] * 100  # (next open - previous close) / previous close


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(percentage) > 2:
    newsparams = {
        "apiKey": newsapi,
        "qInTitle": COMPANY_NAME,
        "from": TODAY - timedelta(days = 2),
        "to": TODAY - timedelta(days = 2)
    }
    response = requests.get(f"https://newsapi.org/v2/everything", params=newsparams)
    response.raise_for_status()
    newsdata = response.json()["articles"]
    nnews = min(3, len(newsdata))
    newsdata = newsdata[:nnews]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    sign = "🔺" if percentage > 0 else "🔻"
    client = Client(smsauth, smstoken)
    for news in newsdata:
        msg = f"{STOCK}{sign}{round(percentage,0)}%\n\n{news['title']}\n\n{news['description']}"
        message = client.messages \
            .create(
            body=msg,
            from_=smsfrom,
            to=smsto
        )
    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

