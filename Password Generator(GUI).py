import random
import string
import math
import tkinter as tk

def generate_password(length=12, upper=True, lower=True, digits=True, special=True):
    characters = ''
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def estimate_entropy(password):
    character_set_size = 0
    if any(c in string.ascii_uppercase for c in password):
        character_set_size += 26
    if any(c in string.ascii_lowercase for c in password):
        character_set_size += 26
    if any(c in string.digits for c in password):
        character_set_size += 10
    if any(c in string.punctuation for c in password):
        character_set_size += 32  # Assuming 32 special characters in string.punctuation

    password_length = len(password)
    entropy = math.log2(character_set_size) * password_length
    return entropy

def generate_passphrase(words=4, separator='-'):
    dictionary = [
        "apple", "banana", "orange", "pear", "grape", "pineapple", "watermelon",
        "carrot", "potato", "tomato", "broccoli", "spinach", "lettuce", "cucumber"
    ]

    passphrase = [random.choice(dictionary).capitalize() for _ in range(words)]
    return separator.join(passphrase)

def generate_password_and_display():
    password_length = int(length_entry.get())
    include_upper = include_upper_var.get()
    include_lower = include_lower_var.get()
    include_digits = include_digits_var.get()
    include_special = include_special_var.get()

    password = generate_password(password_length, include_upper, include_lower, include_digits, include_special)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def generate_passphrase_and_display():
    passphrase_words = int(words_entry.get())
    passphrase = generate_passphrase(passphrase_words)
    passphrase_entry.delete(0, tk.END)
    passphrase_entry.insert(0, passphrase)

# This Is Mandatory For Creating main window
root = tk.Tk()
root.title("Password Generator")

# frame where password Options Are Shown
password_frame = tk.Frame(root)
password_frame.pack(pady=10)

tk.Label(password_frame, text="Password Length:").grid(row=0, column=0, padx=5)
length_entry = tk.Entry(password_frame, width=5)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")  # Default length

include_upper_var = tk.BooleanVar()
include_upper_check = tk.Checkbutton(password_frame, text="Include Uppercase", variable=include_upper_var)
include_upper_check.grid(row=1, column=0, columnspan=2, pady=5)
include_upper_var.set(True)

include_lower_var = tk.BooleanVar()
include_lower_check = tk.Checkbutton(password_frame, text="Include Lowercase", variable=include_lower_var)
include_lower_check.grid(row=2, column=0, columnspan=2, pady=5)
include_lower_var.set(True)

include_digits_var = tk.BooleanVar()
include_digits_check = tk.Checkbutton(password_frame, text="Include Digits", variable=include_digits_var)
include_digits_check.grid(row=3, column=0, columnspan=2, pady=5)
include_digits_var.set(True)

include_special_var = tk.BooleanVar()
include_special_check = tk.Checkbutton(password_frame, text="Include Special Characters", variable=include_special_var)
include_special_check.grid(row=4, column=0, columnspan=2, pady=5)
include_special_var.set(True)

generate_password_button = tk.Button(password_frame, text="Generate Password", command=generate_password_and_display)
generate_password_button.grid(row=5, column=0, columnspan=2, pady=10)

# Entry Spot For Password
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=10)

# Similarly Frame For PassPhrase
passphrase_frame = tk.Frame(root)
passphrase_frame.pack(pady=10)

tk.Label(passphrase_frame, text="Number of Words:").grid(row=0, column=0, padx=5)
words_entry = tk.Entry(passphrase_frame, width=5)
words_entry.grid(row=0, column=1)
words_entry.insert(0, "4")  # Default number of words

generate_passphrase_button = tk.Button(passphrase_frame, text="Generate Passphrase", command=generate_passphrase_and_display)
generate_passphrase_button.grid(row=1, column=0, columnspan=2, pady=10)

# Creating A Passphrase entry field Here
passphrase_entry = tk.Entry(root, width=30)
passphrase_entry.pack(pady=10)

root.mainloop()
#Dunzo!
