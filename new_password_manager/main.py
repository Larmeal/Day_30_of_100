# Upgrade password manager program

from tkinter import *
from tkinter import messagebox
import json
import random

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():

    website = input_website.get()

    try:
        with open("password_manager.json", "r") as data_password:
                read_password = json.load(data_password)
    
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data File Found")

    
    else:
        if len(website) <= 0:
            messagebox.showerror(title="Error", message="Please add the website data")

        elif website not in read_password:
            messagebox.showerror(title="Error", message=f"No data for {website} website")

        else:
            email_show = read_password[f"{website}"]["Email"]
            password_show = read_password[f"{website}"]["Password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email_show} \nPassword: {password_show}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generater():

    password = input_password.get()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = [random.choice(letters) for n in range(random.randint(8, 10))]
    nr_symbols = [random.choice(symbols) for n in range(random.randint(2, 4))]
    nr_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]

    password_list = nr_letters + nr_numbers + nr_symbols
    random.shuffle(password_list)

    combination_password = "".join(password_list)

    if len(password) > 0:
        ask = messagebox.askyesno(title="Waring", message="You need to generate password again? ")
        if ask:
            input_password.delete(0, END)
            input_password.insert(0, combination_password)
    else:
        input_password.insert(0, combination_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data_password = {
        website: {
            "Email": email,
            "Password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Warning", message="Please don't leave any fields empty!") 

    else:
        try:
            with open("password_manager.json", "r") as data_password:
                read_password = json.load(data_password)
        
        except FileNotFoundError:
            with open("password_manager.json", "w") as data_password:
                json.dump(new_data_password, data_password, indent=4)

        else:
            read_password.update(new_data_password)
           
            with open("password_manager.json", "w") as data_password:
                json.dump(new_data_password, data_password, indent=4)

        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Passwork Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_png = PhotoImage(file="new_password_manager/logo.png")

canvas.create_image(100, 100, image=pass_png)
canvas.grid(column=1, row=0)

# website 
website_label = Label(text="Website:", font=("Courier", 10))
website_label.grid(column=0, row=1)

button_search = Button(text="Search", width= 15, command=find_password)
button_search.grid(column=2, row=1)

input_website = Entry(width=22)
input_website.grid(column=1, row=1)
input_website.focus()

# Email
email_label = Label(text="Email/Username:", font=("Courier", 10))
email_label.grid(column=0, row=2)

input_email = Entry(width=41)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "kwang252@hotmail.com")

# Password
password_label = Label(text="Password:", font=("Courier", 10))
password_label.grid(column=0, row=3)

input_password = Entry(width=22)
input_password.grid(column=1, row=3)

button_password = Button(text="Genarate password", width=15, command=generater)
button_password.grid(column=2, row=3)

# Add
button_add_data = Button(text="Add", width=35, command=save)
button_add_data.grid(column=1, row=4, columnspan=3)

window.mainloop()