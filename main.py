import sqlite3
import tkinter as tk
from tkinter import messagebox
from customtkinter import *

connected = False
show_login_page = True

def authenticate_user(username, password, cur):
    global connected, show_login_page
    cur.execute("SELECT * FROM Users WHERE Name=? AND Password=?", (username, password))
    result = cur.fetchone()
    if result is not None:
        connected = True
        show_login_page = False
    return result is not None

def get_employee_status(username, cur):
    cur.execute("SELECT Employee FROM Users WHERE Name=?", (username,))
    result = cur.fetchone()
    return result[0] == 1 if result else False

def show_employee_interface(username, main_window):
    print("welcome admin")
    global connected
    connected = True

def show_user_interface(username, main_window):
    print("welcome user")

def login(usernameEntry, passwordEntry, cur, root):
    username = usernameEntry.get()
    password = passwordEntry.get()

    if authenticate_user(username, password, cur):
        is_employee = get_employee_status(username, cur)
        if is_employee:
            show_employee_interface(username, root)
        else:
            show_user_interface(username, root)
    else:
        messagebox.showerror("Error", "Invalid credentials. Please try again.")

def signup(signup_usernameEntry, signup_passwordEntry, cur, conn):
    is_employee = 0

    new_username = signup_usernameEntry.get()
    cur.execute("SELECT * FROM Users WHERE Name=?", (new_username,))
    existing_user = cur.fetchone()

    if existing_user:
        messagebox.showerror("Error", "Username already taken. Please choose another.")
    else:
        cur.execute("INSERT INTO Users (Name, Password, Employee) VALUES (?, ?, ?)",
                    (new_username, signup_passwordEntry.get(), is_employee))
        conn.commit()
        messagebox.showinfo("Success", "Successfully signed up to Burger Queen")

def main():
    conn = sqlite3.connect("DataBases/Foundation.db")
    cur = conn.cursor()

    root = CTk()
    root.geometry("720x680")
    root.minsize(420, 380)
    root.title("BurgerQueen")
    
    def LoginPage():
        global show_login_page
        if show_login_page:
            title = CTkLabel(root, text="BURGER QUEEN")
            title.pack()

            loginTabs = CTkTabview(root, width=720, height=680)
            loginTabs.pack(padx=20, pady=20)

            loginTabs.add("login")
            loginTabs.add("sign up")

            usernameEntry = CTkEntry(loginTabs.tab("login"), placeholder_text="Username. . .", width=150)
            usernameEntry.place(relx=0.4, rely=0.15)

            passwordEntry = CTkEntry(loginTabs.tab("login"), placeholder_text="Password. . .", show="*", width=150)
            passwordEntry.place(relx=0.4, rely=0.3)

            def on_enter_key(event):
                login(usernameEntry, passwordEntry, cur, root)

            passwordEntry.bind('<Return>', on_enter_key)

            loginButton = CTkButton(loginTabs.tab("login"), text="login", command=lambda: login(usernameEntry, passwordEntry, cur, root))
            loginButton.place(relx=0.4, rely=0.6)

            signup_usernameEntry = CTkEntry(loginTabs.tab("sign up"), placeholder_text="Create Username. . .", width=150)
            signup_usernameEntry.place(relx=0.4, rely=0.15)

            signup_passwordEntry = CTkEntry(loginTabs.tab("sign up"), placeholder_text="Create Password. . .", show="*", width=150)
            signup_passwordEntry.place(relx=0.4, rely=0.3)

            def on_signup_enter_key(event):
                signup(signup_usernameEntry, signup_passwordEntry, cur, conn)

            signup_passwordEntry.bind('<Return>', on_signup_enter_key)

            signInButton = CTkButton(loginTabs.tab("sign up"), text="sign up", command=lambda: signup(signup_usernameEntry, signup_passwordEntry, cur, conn))
            signInButton.place(relx=0.4, rely=0.6)
        else:
            for widget in root.winfo_children():
                widget.destroy()

    def execute_login_page():
        LoginPage()

    def main_loop():
        execute_login_page()
        root.after(1000, main_loop)

    main_loop()

    toggle_button = CTkButton(root, text="Toggle Login Page", command=lambda: LoginPage() if not show_login_page else None)
    toggle_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
