from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    entry3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()

    if website and email and password:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail: {email} \n"
                                                              f"Password: {password} \nSave?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                entry1.delete(0, END)
                entry3.delete(0, END)
    else:
        messagebox.showerror(title="Try Again", message="Please make sure you provided all credentials.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)

entry1 = Entry()
entry1.grid(row=1, column=1, columnspan=2, sticky="EW")
entry1.focus()

entry2 = Entry()
entry2.grid(row=2, column=1, columnspan=2, sticky="EW")
entry2.insert(0, "ishika@email.com")

entry3 = Entry()
entry3.grid(row=3, column=1, sticky="EW")

button1 = Button(text="Generate Password", command=generate_password)
button1.grid(row=3, column=2, sticky="EW")

button2 = Button(text="Add", width=36, command=save)
button2.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
