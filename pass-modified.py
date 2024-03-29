from tkinter import *
import random, string
import pyperclip

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(pass_len.get()))
    pass_str.set(password)

def copy_password():
    pyperclip.copy(pass_str.get())
    copy_label.config(text="Copied!", fg="green")

root = Tk()
root.geometry("300x200")
root.title("Password Generator")

pass_len = IntVar(value=12)

Label(root, text='Password Length:').pack()
Spinbox(root, from_=8, to_=32, textvariable=pass_len).pack(pady=5)

Button(root, text="Generate Password", command=generate_password, bg="skyblue").pack(pady=5)
pass_str = StringVar()
Entry(root, textvariable=pass_str, width=20, state='readonly', relief='flat').pack(pady=5)

Button(root, text='Copy to Clipboard', command=copy_password, bg="lightgreen").pack(pady=5)
copy_label = Label(root, text='', fg="green")
copy_label.pack()

root.mainloop()
