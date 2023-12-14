import sqlite3
import tkinter as tk
import customtkinter
from customtkinter import *



#connecting to the database
conn = sqlite3.connect('C:/Tiller VG 2/Yrkesfag/Utvikling/burgerQueen/DataBases/foundation.db')
cur = conn.cursor()

#APP SETUP
root = CTk()
root.geometry("720x680")
root.minsize(420, 380)
root.title("BurgerQueen")

#Login screen
title = customtkinter.CTkLabel(root, text="BURGER QUEEN")  #Text inside the program that says 'BURGER QUEEN'
title.pack() #.pack organizes the elements position, it is required to finish editing an element, always remember to pack your element.

loginTabs = CTkTabview(
    root,
    width=720,
    height=680)
loginTabs.pack(padx=20, pady=20)

loginTabs.add("login")
loginTabs.add("sign up")

#LOGIN
usernameEntry = CTkEntry(loginTabs.tab("login"), placeholder_text="Username. . .", width=150)
usernameEntry.place(relx=0.4, rely=0.15)

passwordEntry = CTkEntry(loginTabs.tab("login"), placeholder_text="Password. . .", show="*", width=150)
passwordEntry.place(relx=0.4, rely=0.3)

def login():
    print("you've logged in!")

loginButton = customtkinter.CTkButton(
    loginTabs.tab("login"),
    text="login",
    command=login
)
loginButton.place(relx=0.4, rely=0.6)

#SIGNIN
usernameEntry = CTkEntry(loginTabs.tab("sign up"), placeholder_text="Create Username. . .", width=150)
usernameEntry.place(relx=0.4, rely=0.15)

passwordEntry = CTkEntry(loginTabs.tab("sign up"), placeholder_text="Create Password. . .", show="*", width=150)
passwordEntry.place(relx=0.4, rely=0.3)

def signup():
    print("you've signed in!")

signInButton = customtkinter.CTkButton(
    loginTabs.tab("sign up"),
    text="sign up",
    command=signup
)

signInButton.place(relx=0.4, rely=0.6)
#executes the program with GUI
root.mainloop()