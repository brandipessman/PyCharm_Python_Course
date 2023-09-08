from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols +password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
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
        messagebox.showerror(title = "Empty Entry", message = "Please enter a website and password.")
    else:
        # is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered: \nEmail: {email}"
        #                                                   f"\nPassword: {password}\nIs it ok to save?")
        # if is_ok:
        # with open("my_vault.txt", mode = "a") as data:
            # data.write(f"{website} | {email} | {password} \n")
        try:
            with open("my_vault.json", mode= "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("my_vault.json", "w") as data_file:
                # Open new file
                json.dump(new_data, data_file, indent = 4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("my_vault.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("my_vault.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title = "Error", message = f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)

canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website: ")
website_label.grid(row = 1, column = 0)

email_label = Label(text = "Email/Username: ")
email_label.grid(row = 2, column = 0)

password_label = Label(text = "Password: ")
password_label.grid(row = 3, column = 0)

website_entry = Entry(width = 21)
website_entry.grid(row = 1, column = 1, columnspan = 1)
website_entry.focus()

email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 2)
email_entry.insert(0, "@gmail.com")

password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1, columnspan = 1)

gen_pw = Button(text = "Generate Password", width = 15, command = generate_password)
gen_pw.grid(row = 3, column = 2)

add = Button(text = "Add", width = 36, command = save)
add.grid(row = 4, column = 1, columnspan = 2)

search = Button(text = "Search", width = 15, command = find_password)
search.grid(row = 1, column = 2)

window.mainloop()