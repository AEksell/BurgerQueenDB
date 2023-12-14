import sqlite3
import tkinter as tk
import customtkinter
from tkinter import messagebox
from customtkinter import *

# Connecting to the database
conn = sqlite3.connect("C:/Users/leona/OneDrive/Skrivebord/IT 2/Utvikling1/burgerqueenprosjekt/DataBases/Foundation.db")
cur = conn.cursor()

# APP SETUP
root = CTk()
root.geometry("720x680")
root.minsize(420, 380)
root.title("BurgerQueen")

# LOGIN SCREEN
title = CTkLabel(root, text="BURGER QUEEN")
title.pack()

loginTabs = CTkTabview(root, width=720, height=680)
loginTabs.pack(padx=20, pady=20)

loginTabs.add("login")
loginTabs.add("sign up")

# LOGIN
usernameEntry = CTkEntry(loginTabs.tab("login"), placeholder_text="Username. . .", width=150)
usernameEntry.place(relx=0.4, rely=0.15)

passwordEntry = CTkEntry(loginTabs.tab("login"), placeholder_text="Password. . .", show="*", width=150)
passwordEntry.place(relx=0.4, rely=0.3)

def on_enter_key(event):
    # This function is called when the Enter key is pressed
    login()

# Bind the Enter key to the password entry widget
passwordEntry.bind('<Return>', on_enter_key)

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    
    if authenticate_user(username, password):
        is_employee = get_employee_status(username)
        if is_employee:
            # Show employee interface
            show_employee_interface()
        else:
            # Show user interface
            show_user_interface()
    else:
        # Display an error message using a popup box
        messagebox.showerror("Error", "Invalid credentials. Please try again.")

def authenticate_user(username, password):
    cur.execute("SELECT * FROM Users WHERE Name=? AND Password=?", (username, password))
    result = cur.fetchone()
    return result is not None

def get_employee_status(username):
    cur.execute("SELECT Employee FROM Users WHERE Name=?", (username,))
    result = cur.fetchone()
    return result[0] == 1 if result else False

def show_employee_interface():
    # Add functionality for the employee interface
    print("Welcome, employee!")

def show_user_interface():
    # Add functionality for the normal user interface
    print("Welcome, user!")

loginButton = CTkButton(loginTabs.tab("login"), text="login", command=login)
loginButton.place(relx=0.4, rely=0.6)

# SIGN UP
signup_usernameEntry = CTkEntry(loginTabs.tab("sign up"), placeholder_text="Create Username. . .", width=150)
signup_usernameEntry.place(relx=0.4, rely=0.15)

signup_passwordEntry = CTkEntry(loginTabs.tab("sign up"), placeholder_text="Create Password. . .", show="*", width=150)
signup_passwordEntry.place(relx=0.4, rely=0.3)

def on_signup_enter_key(event):
    # This function is called when the Enter key is pressed for signup
    signup()

# Bind the Enter key to the password entry widget for signup
signup_passwordEntry.bind('<Return>', on_signup_enter_key)

def signup():
    # By default, new signups are normal users
    is_employee = 0

    # Check if the username already exists
    new_username = signup_usernameEntry.get()
    cur.execute("SELECT * FROM Users WHERE Name=?", (new_username,))
    existing_user = cur.fetchone()

    if existing_user:
        messagebox.showerror("Error", "Username already taken. Please choose another.")
    else:
        # Insert the new user into the database
        cur.execute("INSERT INTO Users (Name, Password, Employee) VALUES (?, ?, ?)",
                    (new_username, signup_passwordEntry.get(), is_employee))
        conn.commit()
        print("You've signed up as a user!")

signInButton = CTkButton(loginTabs.tab("sign up"), text="sign up", command=signup)
signInButton.place(relx=0.4, rely=0.6)

# executes the program with GUI
root.mainloop()
