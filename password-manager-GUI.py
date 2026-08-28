import getpass
from crypto import encrypt_pw, decrypt_pw
import json
import os
import random
import string
import tkinter as tk
from tkinter import messagebox

password_file = "passwords.json"
managed_passwords = {}


#logic functions

def save_passwords():
    with open(password_file, "w") as f:
        json.dump(managed_passwords, f)         #store the encrypted passwords(as strings)

def load_passwords():
    if os.path.exists(password_file):
        with open(password_file, "r") as f:
            return json.load(f)
    else:
        return {}

def generate_pw(length=12):
    chars = string.ascii_letters + string.punctuation + string.digits 
    password = "".join(random.choice(chars) for _ in range(length))
    return password

# GUI functions

# GUI setup
root = tk.Tk()
root.title("Password Manager")
root.geometry("800x500")

# home page
# create account page
# login page
# view passwords page
# delete account page

root.mainloop()