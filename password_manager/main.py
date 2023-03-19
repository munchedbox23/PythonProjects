from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
path = "password_manager/data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passoword_letters = [random.choice(letters) for  _ in range(random.randint(8,10))]
    passoword_numbers = [random.choice(numbers) for  _ in range(random.randint(2,4))]
    passoword_symbols = [random.choice(symbols) for  _ in range(random.randint(2,4))]

    password_list = passoword_letters + passoword_numbers + passoword_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(path, mode = "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(path, mode ="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open(path, "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
         with open(path,"r") as data_file:
                data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Менеджер паролей")
window.config(padx = 50, pady = 50)
window.resizable(False,False)

logo_image = PhotoImage(file = "password_manager/logo.png")
canvas = Canvas(width = 200, height=200)
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column = 1, row = 0)

# Create Label
website_label = Label(window,text = "Веб-сайт:")
website_label.grid(column = 0 , row = 1)
username_label = Label(window,text = "Почта/Логин:")
username_label.grid(column = 0 , row = 2)
password_label = Label(window,text = "Пароль")
password_label.grid(column = 0 , row = 3)

# Create Entries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1,sticky="e")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=25,show="*")
password_entry.grid(row=3, column=1,sticky="e")


# Create Buttons
search_button = Button(text = "Search",width= 13,command = find_password)
search_button.grid(row=1,column = 2)
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
