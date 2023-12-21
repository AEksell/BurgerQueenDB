import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import Scrollbar
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from CTkTable import *
import time

connected = False
show_login_page = True
conn = sqlite3.connect("DataBases/Foundation.db")
cur = conn.cursor()

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

def Refresh_Ingredients_data(ingredients_table, ingredients_result):
    cur.execute("SELECT * FROM Ingredients")
    ingredients_result = cur.fetchall()

    ingredients_data = [list(row) for row in ingredients_result]
    print(ingredients_data)
    ingredients_table.update_values(ingredients_data)

def OrderStatus(orderlist, orderTable):
    cur.execute("SELECT * FROM Orders")
    orderlist = cur.fetchall()
    
    orderTable = [list(row) for row in orderlist]
    print(orderTable)

        
def show_employee_interface(username, main_window, ):
    global root
    global OptionTabs

    for widget in main_window.winfo_children():
        widget.destroy()
    show_user_interface(username, main_window)

    title = CTkLabel(root, text="HI ADMIN")
    title.pack()

    OptionTabs.add("Ingredients")
    OptionTabs.add("Orders")

    # Retrieve ingredients data from the database
    cur.execute("SELECT * FROM Ingredients")
    ingredients_result = cur.fetchall()

    # Create a list of ingredients data
    ingredients_data = [list(row) for row in ingredients_result]

    # Create a frame to contain the ingredients table
    ingredients_frame = CTkFrame(OptionTabs.tab("Ingredients"))
    ingredients_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Create a canvas to simulate a scrollable frame
    ingredients_canvas = CTkCanvas(ingredients_frame)
    ingredients_canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar for the canvas
    ingredients_scrollbar = Scrollbar(ingredients_frame, orient="vertical", command=ingredients_canvas.yview)
    ingredients_scrollbar.pack(side="right", fill="y")
    ingredients_canvas.configure(yscrollcommand=ingredients_scrollbar.set)

    # Create a frame inside the canvas to hold the ingredients table
    ingredients_interior = CTkFrame(ingredients_canvas)
    ingredients_canvas.create_window((0, 0), window=ingredients_interior, anchor="nw")

    # Create the ingredients table inside the frame
    ingredients_table = CTkTable(
        ingredients_interior,
        width = 200,
        height = 80,
        row=len(ingredients_data),
        column=len(ingredients_data[0]),
        values=ingredients_data,
        hover_color="#2D419C"
    )
    ingredients_table.pack(expand=True, fill="both")

    # Configure the canvas to update scroll region when the table size changes
    ingredients_interior.update_idletasks()
    ingredients_canvas.config(scrollregion=ingredients_canvas.bbox("all"))
    
    # Retrieve orders data from the database
    cur.execute("SELECT Orders.OrderID, Users.Name AS CustomerName, Burgers.Name AS BurgerName, CASE Orders.Produced WHEN 1 THEN 'Yes' ELSE 'No' END AS Produced FROM Orders JOIN Users ON Orders.CustomerID = Users.UserID JOIN Burgers ON Orders.BurgerID = Burgers.BurgerID;")
    orderlist = cur.fetchall()
    orderTable = [list(row) for row in orderlist]

    # Insert column names as the first row in the orderTable
    column_names = ["Order ID", "Customer Name", "Product", "Finished"]  # Replace with your column names
    orderTable.insert(0, column_names)

    # Make orders table GUI (SIMILAR TO INGREDIENTS TABLE CREATION)
    OrdersFrame = CTkFrame(OptionTabs.tab("Orders"))
    OrdersFrame.pack(expand=True, fill="both", padx=20, pady=20)

    OrdersCanvas = CTkCanvas(OrdersFrame, bg="#212121")
    OrdersCanvas.pack(side="left", fill="both", expand=True)

    OrdersScrollbar = Scrollbar(OrdersFrame, orient="vertical", command=OrdersCanvas.yview)
    OrdersScrollbar.pack(side="right", fill="y")
    OrdersCanvas.configure(yscrollcommand=OrdersScrollbar.set)

    OrdersInterior =  CTkFrame(OrdersCanvas)
    OrdersCanvas.create_window((0, 0), window=OrdersInterior, anchor="nw")

    OrdersTable = CTkTable(
    OrdersInterior,
    width=150,
    height=90,
    row=len(orderTable),
    column=len(orderTable[0]),
    values=orderTable,
    hover_color="#2D419C",
    )

    OrdersTable.pack(expand=True, fill="both")
        
    def update_produced():
        buttonlabel = 0
        try:
            selected_order_id = selectOrderComplete.get()
            cur.execute("UPDATE Orders SET Produced = CASE WHEN Produced = 1 THEN 0 ELSE 1 END WHERE OrderID = ?", (selected_order_id,))
            conn.commit()
            #print(selected_order_id)

            # Refresh the entire table after database update
            cur.execute("SELECT Orders.OrderID, Users.Name AS CustomerName, Burgers.Name AS BurgerName, CASE Orders.Produced WHEN 1 THEN 'Yes' ELSE 'No' END AS Produced FROM Orders JOIN Users ON Orders.CustomerID = Users.UserID JOIN Burgers ON Orders.BurgerID = Burgers.BurgerID;")
            orderlist = cur.fetchall()
            orderTable = [list(row) for row in orderlist]
            orderTable.insert(0, ["Order ID", "Customer Name", "Product", "Finished"])
            ++buttonlabel

            if buttonlabel < 2:
                OrderChangeMessage = CTkLabel(OptionTabs.tab("Orders"), text="To see the differences youve made to the database,\n please reOpen the software.", text_color="red", font=('Arial', 10))
                OrderChangeMessage.place(relx=0.01, rely=0.85)
       
            update_order_and_ingredients(selected_order_id)
        
        except Exception as e:
            print(f"Error occurred: {e}")
            conn.rollback()

    def update_order_and_ingredients(selected_order_id):

        # Check if the order is produced
        cur.execute("SELECT Produced, BurgerID FROM Orders WHERE OrderID = ?", (selected_order_id,))
        result = cur.fetchone()

        if result and result[0] == 3:  # Assuming 1 represents 'Produced'
            burger_id = result[1]

            # Update the order status
            cur.execute("UPDATE Orders SET Produced = 1 WHERE OrderID = ?", (selected_order_id,))

            # Get the list of ingredient descriptions for the burger
            cur.execute("SELECT Ingredients FROM Burgers WHERE BurgerID = ?", (burger_id,))
            ingredients_list = cur.fetchone()

            # Update the quantity for each ingredient in the list
            if ingredients_list:
                ingredient_descriptions = ingredients_list[0].split(', ')
                for ingredient_description in ingredient_descriptions:
                    cur.execute("UPDATE Ingredients SET Quantity = Quantity - 1 WHERE Ingredient = ?", (ingredient_description,))

                # Commit the changes
                conn.commit()
                print(f"Order {selected_order_id} produced and ingredients updated.")
            else:
                print(f"Unable to retrieve ingredients for BurgerID {burger_id}.")
        else:
            print(f"Order {selected_order_id} not produced.")




    cur.execute("SELECT OrderID FROM Orders")
    selectOrderList = cur.fetchall()
    orderIDs = [str(order[0]) for order in selectOrderList]

    orderboxLabel = CTkLabel(OptionTabs.tab("Orders"), text="Select Order")
    orderboxLabel.place(relx=0.441, rely=0.8)

    selectOrderComplete = CTkComboBox(OptionTabs.tab("Orders"), values=orderIDs, state="readonly")
    selectOrderComplete.pack(padx=5, pady=10)
    
    ConfirmOrderChangeButton = CTkButton(OptionTabs.tab("Orders"), text="Declare Order finished/Unfinished", command=update_produced)
    ConfirmOrderChangeButton.pack(padx=5, pady=10)

def show_user_interface(username, main_window):
    global root
    global OptionTabs
    
    for widget in main_window.winfo_children():
        widget.destroy()
        
    OptionTabs = CTkTabview(
        root,
        width=720,
        height=680,
    )
    OptionTabs.pack(padx=20, pady=20)
    
    OptionTabs.add("My orders")
    OptionTabs.add("Order")
    
    logoutButton = CTkButton(
        root,
        text="Logout",
        corner_radius=25,
        width=30,
        command=lambda: logout(main_window))
    logoutButton.place(relx=0.8, rely=0.035)
    

def logout(main_window):
    global show_login_page, connected
    for widget in main_window.winfo_children():
        widget.destroy()
    show_login_page = True  
    connected = False  
    LoginPage()

def LoginPage():
    global show_login_page
    conn = sqlite3.connect("DataBases/Foundation.db")
    cur = conn.cursor()
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
        CTkMessagebox(title="Error", message="Invalid credentials. Please try again.", icon="cancel")

def signup(signup_usernameEntry, signup_passwordEntry, cur, conn):
    global connected, show_login_page
    is_employee = 0

    new_username = signup_usernameEntry.get()
    cur.execute("SELECT * FROM Users WHERE Name=?", (new_username,))
    existing_user = cur.fetchone()

    if existing_user:
        CTkMessagebox(title="Error", message="Username already taken. Please choose another.",icon="cancel")
    else:
        cur.execute("INSERT INTO Users (Name, Password, Employee) VALUES (?, ?, ?)",
                    (new_username, signup_passwordEntry.get(), is_employee))
        conn.commit()
        CTkMessagebox(title="Success", message="Successfully signed up to Burger Queen",icon="check",option_1="continue" )
        connected = True
        show_login_page = False


def main():
    global root
    conn = sqlite3.connect("DataBases/Foundation.db")
    cur = conn.cursor()

    root = CTk()
    root.geometry("720x680")
    root.minsize(420, 380)
    root.title("BurgerQueen")
    
    
    set_default_color_theme("dark-blue")
    set_appearance_mode("dark")
    

    def execute_login_page():
        LoginPage()

    def main_loop():
        execute_login_page()
        root.after(1000, main_loop)

    #OPENS AFTER LOGIN
    main_loop()
    root.mainloop()

if __name__ == "__main__":
    main()

