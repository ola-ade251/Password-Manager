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

def create_account_gui():
    username = create_username_entry.get()
    password = create_password_entry.get()

    if username in managed_passwords:
        messagebox.showerror("Error", "Username already exists, make another one.")
        return
    if password.strip() == "":
        messagebox.showerror("Error", "Password cant be empty.")
        return

    encrypted = encrypt_pw(password)
    managed_passwords[username] = encrypted
    save_passwords()

    messagebox.showinfo("success", "Account created")
    create_username_entry.delete(0, tk.END)
    create_password_entry.delete(0, tk.END)


def login_gui():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if username not in managed_passwords:
        messagebox.showerror("Error", "username not found")
        return
    stored_encrypted = managed_passwords[username]
    stored_original = decrypt_pw(stored_encrypted)

    if password == stored_original:
        messagebox.showinfo("Success", "login successful")
    else:
        messagebox.showerror("Error", "login failed")


def delete_gui():
    username = delete_username_entry.get()
    if username not in managed_passwords:
        messagebox.showerror("Error", "username not found")
        return
        
    confirm = messagebox.askyesno("Confirm", f"Delete account '{username}'?")
    if confirm:
        del managed_passwords[username]
        save_passwords()
        messagebox.showinfo("Success", "account deleted")



def generate_pw_gui():
    pw= generate_pw()
    messagebox.showinfo("generated password", pw)
    create_password_entry.delete(0, tk.END)
    create_password_entry.insert(0, pw)

    
def view_gui():
    view_text.delete("1.0", tk.END)
    for user, encrypted in managed_passwords.items():
        original = decrypt_pw(encrypted)
        view_text.insert(tk.END, f"{user}: {original}\n")




# GUI setup

root = tk.Tk()
root.title("Password Manager")
root.geometry("800x500")

managed_passwords = load_passwords()

#frames
home_frame = tk.Frame(root)
create_frame = tk.Frame(root)
login_frame = tk.Frame(root)
view_frame = tk.Frame(root)
del_frame = tk.Frame(root)

for frame in (home_frame, create_frame, login_frame, view_frame, del_frame):
    frame.grid(row =0, column =0, sticky= "nsew")

# home page
home_label=tk.Label(home_frame, text= "Password Manager", font=('Arial, 18'))
home_label.pack(padx=20, pady=20)
# buttons that lead to other pages
create_btn= tk.Button(home_frame, text="Create Account", command= lambda: create_frame.tkraise())   #show the create frame-create page
create_btn.pack(padx=20, pady=20)
login_btn= tk.Button(home_frame, text="Login", command= lambda: login_frame.tkraise())
login_btn.pack(padx=20, pady=20)
view_btn= tk.Button(home_frame, text="View Passwords", command= lambda: view_frame.tkraise())
view_btn.pack(padx=20, pady=20)
del_btn= tk.Button(home_frame, text="Delete Account", command= lambda: del_frame.tkraise())
del_btn.pack(padx=20, pady=20)
generate_btn= tk.Button(home_frame, text="Generate Password", command= generate_pw_gui )  
generate_btn.pack(padx=20, pady=20)


# create account page
c_label = tk.Label(create_frame, text = "Create Account", font = ('Arial', 18))
c_label.pack(padx=20, pady=20)

user_label=tk.Label(create_frame, text= "username")
user_label.pack()
create_username_entry = tk.Entry(create_frame)
create_username_entry.pack()

user_label=tk.Label(create_frame, text= "password")
user_label.pack()
create_password_entry = tk.Entry(create_frame)
create_password_entry.pack()

tk.Button(create_frame, text="Generate Password", command=generate_pw_gui).pack(padx=10, pady=10)
tk.Button(create_frame, text="Save Account", command=create_account_gui).pack(padx=10, pady=10)
tk.Button(create_frame, text="Back", command=lambda: home_frame.tkraise()).pack(padx=10, pady=10)


# login page
l_label = tk.Label(login_frame, text = "Login", font = ('Arial', 18))
l_label.pack(padx=20, pady=20)

user_label=tk.Label(login_frame, text= "username")
user_label.pack()
login_username_entry = tk.Entry(login_frame)
login_username_entry.pack()

user_label=tk.Label(login_frame, text= "password")
user_label.pack()
login_password_entry = tk.Entry(login_frame)
login_password_entry.pack()

tk.Button(login_frame, text="Login", command=login_gui).pack(padx=10, pady=10)
tk.Button(login_frame, text="Back", command=lambda: home_frame.tkraise()).pack(padx=10, pady=10)


# view passwords page
v_label = tk.Label(view_frame, text = "Stored Passwords", font = ('Arial', 18))
v_label.pack(padx=20, pady=20)

view_text = tk.Text(view_frame, height = 15, width=50)
view_text.pack(padx=20, pady=20)

tk.Button(view_frame, text="Refresh", command=view_gui).pack(padx=10, pady=10)
tk.Button(view_frame, text="Back", command=lambda: home_frame.tkraise()).pack(padx=10, pady=10)


# delete account page
d_label = tk.Label(del_frame, text = "Delete Account", font = ('Arial', 18))
d_label.pack(padx=20, pady=20)

d_label=tk.Label(del_frame, text= "username")
d_label.pack()
delete_username_entry = tk.Entry(del_frame)
delete_username_entry.pack()

tk.Button(del_frame, text="Delete", command=delete_gui).pack(padx=10, pady=10)
tk.Button(del_frame, text="Back", command=lambda: home_frame.tkraise()).pack(padx=10, pady=10)



home_frame.tkraise()        #  start with home page
root.mainloop()