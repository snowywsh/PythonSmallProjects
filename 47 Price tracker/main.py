from bs4 import BeautifulSoup
import requests
import pandas as pd
import smtplib as sb


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
fromemail = "verageweixiang@gmail.com"
passwd = "PjGuuQti3296*#*"
toemail = "snowywsh@gmail.com"
items = pd.read_csv("items.csv").to_dict(orient="records")
# print(items)

# item = items[0]
# # print(item)
for item in items:
    response = requests.get(url=item['url'], headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    price = soup.find(id="priceblock_ourprice").getText()
    price = float(price[1:])
    title = soup.find(id="productTitle").get_text().strip() # getText()
    if price < item['price']:
        msg = f"{title} is now below {item['price']}.\n\n{item['url']}"
        # print(msg.encode('utf8'))
        with sb.SMTP("smtp.gmail.com") as connection:  # no need connection.close() in this way
            connection.starttls()  # make the transfer secure
            connection.login(user=fromemail, password=passwd)
            connection.sendmail(from_addr=fromemail,
                                to_addrs=toemail,
                                msg=f"Subject:Amazon Price Alter!\n\n{msg}".encode('utf8'))
