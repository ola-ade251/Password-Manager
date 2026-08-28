from cryptography.fernet import Fernet

key_file = "key.key"        #name of file that will hold the encyption key

def generate_key():
    key = Fernet.generate_key()         #create an encyption key(master key), and write it into the key file
    with open(key_file, "wb") as f:
        f.write(key)

def load_key():
    with open(key_file, "rb") as f:     #read e.key and return so its used
        return f.read()

def encrypt_pw(password):
    key = load_key()
    f = Fernet(key)                     #use key to make fernet encyption- symmetrical
    encrypted = f.encrypt(password.encode())            #pw turned into bytes and encrypted
    return encrypted.decode()           #converts encrypted back into string from bytes for storage in dict

def decrypt_pw(encrypted_pw):           # turn encypted password back to original
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_pw.encode())
    return decrypted.decode()
