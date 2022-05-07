from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip
import json
import sys


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def clickGen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pswdletters = [rd.choice(letters) for _ in range(rd.randint(8, 10))]
    pswdnumbers = [rd.choice(numbers) for _ in range(rd.randint(2, 4))]
    pswdsymbols = [rd.choice(symbols) for _ in range(rd.randint(2, 4))]

    pswdlist = pswdletters + pswdnumbers + pswdsymbols
    rd.shuffle(pswdletters + pswdnumbers + pswdsymbols)
    password = "".join(pswdlist)
    # print(f"Your password is: {password}")
    pswdentry.insert(0, password)
    pyperclip.copy(password)

def clickSearch():
    website = websiteentry.get()
    if getattr(sys, "frozen", False):
        filepath = os.path.join(sys._MEIPASS, "data.json")
    else:
        filepath = "data.json"
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File is empty.")
    else:
        if website in data:
            urname = data[website]["urname"]
            pswd = data[website]["pswd"]
            messagebox.showinfo(title=website, message=f"Username: {urname}\nPassword: {pswd}\n")
        else:
            messagebox.showinfo(title="Error", message=f"{website} is not in the file.")
    finally:
        websiteentry.delete(0, END)
        pswdentry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clickAdd():
    website = websiteentry.get()
    urname = urnameentry.get()
    pswd = pswdentry.get()
    newjson = {
        website: {
            "urname": urname,
            "pswd": pswd
        }
    }
    if not website or not urname or not pswd:
        messagebox.showinfo(title="Oops", message="Please make sure every field is filled!")
    else:
        save = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {urname}\nPassword: {pswd}\nIs it OK to save?")
        if save:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(newjson, file, indent=4)
            else:
                data.update(newjson)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                websiteentry.delete(0, END)
                pswdentry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
if getattr(sys, "frozen", False):
    logoimg = PhotoImage(file=os.path.join(sys._MEIPASS, "logo.png"))
else:
    logoimg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoimg)
canvas.grid(row=0, column=1)

websitelabel = Label(text="Website: ")
websitelabel.grid(row=1, column=0)
websiteentry = Entry(width=21)
websiteentry.grid(row=1, column=1)
websiteentry.focus()

urnamelabel = Label(text="Email/Username: ")
urnamelabel.grid(row=2, column=0)
urnameentry = Entry(width=35)
urnameentry.grid(row=2, column=1, columnspan=2)
urnameentry.insert(END, "example@gmail.com")

pswdlabel = Label(text="Password: ")
pswdlabel.grid(row=3, column=0)
pswdentry = Entry(width=21)
pswdentry.grid(row=3, column=1)

genpswd = Button(text="Generate Password", command=clickGen)
genpswd.grid(row=3, column=2)

addpswd = Button(text="Add", width=35, command=clickAdd)
addpswd.grid(row=4, column=1, columnspan=2)

searchpswd = Button(text="Search", width=13, command=clickSearch)
searchpswd.grid(row=1, column=2)

window.mainloop()
