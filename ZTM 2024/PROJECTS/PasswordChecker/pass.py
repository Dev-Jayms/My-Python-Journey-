# create a user interface using a library like Tkinter or PyQt to allow users to input their passwords and check if they have been leaked.

# This code creates a simple window with a label, a text entry field, and two buttons. The "Check Password" button checks if the password in the text entry field has been leaked, and the "Generate Password" button generates a new random password and inserts it into the text entry field.
import tkinter as tk
from tkinter import messagebox
import hashlib
import requests


def check_password(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code == 200:
        for line in response.text.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return True
    return False


def check_password_button_clicked():
    password = password_entry.get()
    if password:
        is_leaked = check_password(password)
        if is_leaked:
            messagebox.showerror(
                "Password Leaked", "Your password has been leaked!")
        else:
            messagebox.showinfo("Password Safe", "Your password is safe!")
    else:
        messagebox.showerror("Error", "Please enter a password!")


def generate_password_button_clicked():
    import secrets
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


root = tk.Tk()
root.title("Password Checker")

password_label = tk.Label(root, text="Enter your password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

check_password_button = tk.Button(
    root, text="Check Password", command=check_password_button_clicked)
check_password_button.pack()

generate_password_button = tk.Button(
    root, text="Generate Password", command=generate_password_button_clicked)
generate_password_button.pack()

root.mainloop()
