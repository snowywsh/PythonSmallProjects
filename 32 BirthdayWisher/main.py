import smtplib as sl

myemail = "verageweixiang@gmail.com"
password = "PjGuuQti3296*#*"
#

#     # connection.close()

import datetime as dt
import random as rd

def sendEmail():
    with open("quotes.txt", "r") as quotes:
        allquotes = quotes.readlines()
        quote = rd.choice(allquotes)
        msg = "subject:hello\n\n"+quote
    print(msg)
    with sl.SMTP("smtp.gmail.com") as connection: # no need connection.close() in this way
        connection.starttls()  # make the transfer secure
        connection.login(user=myemail, password=password)
        connection.sendmail(from_addr=myemail,
                            to_addrs=myemail,
                            msg=msg.encode("utf8"))

today = dt.datetime.now()
if today.weekday() == 3:
    sendEmail()




