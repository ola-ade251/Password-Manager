import getpass
from crypto import encrypt_pw, decrypt_pw
import json
import os


password_file = "passwords.json"
managed_passwords ={}
#"username1": "password1"
#"username2": "password2"

def main():     #menu screen
    global managed_passwords
    managed_passwords = load_passwords()
    while True:
        choice = input("type 1 for create account, 2 for login 3 to view pws and 4 to exit")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            view_pws()
        elif choice == "4":
            print("exiting")
            break
        else:
            print("invalid input: choose from either 1, 2 or 3")
        

def create_account():
    username = input("create username")
    if username in managed_passwords:
        print("username already exists, create another.")
        return
    password = getpass.getpass("create password")
    encrypted = encrypt_pw(password)
    managed_passwords[username] = encrypted
    save_passwords()
    print("account created!")

def login():
    username = input("enter username")
    if username not in managed_passwords:
        print("username not found")
        return
    password = getpass.getpass("enter password")
    stored_encrypted = managed_passwords[username]
    stored_original = decrypt_pw(stored_encrypted)
    if password == stored_original:      # if username and password match to the hash, successful
        print("login successful!")
    else:
        print("login failed")

def view_pws():
    print("\nstored passwords:")
    for user, encrypted in managed_passwords.items():       # loop through every username and its encrypted pw
        original_pw = decrypt_pw(encrypted)
        print(f"{user}: {original_pw}")

def save_passwords():
    with open(password_file, "w") as f:
        json.dump(managed_passwords, f)         #store the encrypted passwords(as strings)

def load_passwords():
    if os.path.exists(password_file):
        with open(password_file, "r") as f:
            return json.load(f)
    else:
        return {}


main()