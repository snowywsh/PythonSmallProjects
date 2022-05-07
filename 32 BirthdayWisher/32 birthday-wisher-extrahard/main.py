##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib as sb
import random as rd

myemail = "verageweixiang@gmail.com"
password = "PjGuuQti3296*#*"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
todayTuple = (today.month, today.day)

people = pd.read_csv("birthdays.csv")

# this way does not work for duplicate birthday, so use the one beolw
birthday = {(person["month"], person["day"]): person for (index, person) in people.iterrows()}

birthday = {}
for (index, person) in people.iterrows():
    birthday.setdefault((person["month"], person["day"]), [])
    birthday[(person["month"], person["day"])].append(person)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if todayTuple in birthday:
    for person in birthday[todayTuple]:
        letter = f"letter_templates/letter_{rd.randint(1, 3)}.txt"
        with open(letter) as letterfile:
            content = letterfile.read()
            content = content.replace("[NAME]", person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with sb.SMTP("smtp.gmail.com") as connection:  # no need connection.close() in this way
            connection.starttls()  # make the transfer secure
            connection.login(user=myemail, password=password)
            connection.sendmail(from_addr=myemail,
                                to_addrs=person["email"],
                                msg=f"subject:hello\n\n{content}")

"""
to run this every day, go to pythonanywhere.com, 
upload the files as in the folder, i.e. main.py, birthday.csv, and (all letter templates) in a folder, 
schedule it to run on the cloud with command: python3 main.py  
"""




