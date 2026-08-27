import hashlib
import getpass


managed_passwords ={}
#"username1": "password1"
#"username2": "password2"

def main():     #menu screen
    
    while True:
        choice = input("type1 for create account, 2 for login and 3 to exit")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("exiting")
            break
        else:
            print("invalid input: choose from either 1, 2 or 3")
        
def hash(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest() #store all hashed passwords in managed passwords
    return hashed_password

def create_account():
    username = input("create username")
    if username in managed_passwords:
        print("username already exists, create another.")
        return
    password = getpass.getpass("create password")
    hashed_pw = hash(password)
    managed_passwords[username] = hashed_pw
    print("account created!")

def login():
    username = input("enter username")
    if username not in managed_passwords:
        print("username not found")
        return
    password = getpass.getpass("enter password")
    hashed_pw = hash(password)
    if managed_passwords[username] == hashed_pw:       # if username and password match to the hash, successful
        print("login successful!")
    else:
        print("login failed")

main()