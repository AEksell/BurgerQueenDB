# Burger Queen Application

- [Dependencies](#dependencies)
- [Imports](#imports)
- [Features](#features)
  - [User Interface](#user-interface)
  - [Employee Interface](#employee-interface)
- [How to Run](#how-to-run)
- [Usage](#usage)

- [Notes](#notes)
## Dependencies

- `CustomTkinter`:Customized tkinter elements for enhanced appearance.

  pip3 install customtkinter
  pip install customtkinter --upgrade

- `CTkMessagebox`:Customized messagebox for displaying messages.

  pip install CTkMessagebox

- `CTkTable`:Customized table for displaying data in tabular format.

  pip install CTkTable


## Imports

- `Import time`
  
- `Import CTkTable`

- `Import CTkMessagebox`

- `Import customtkinter`

- `Import sqlite3`



## Features


### User Interface

1. **Login/Signup:** Users can log in with their existing credentials or sign up for a new account.

2. **Place Orders:** Users can choose a burger from the menu, specify the quantity, and place an order.

3. **View Orders:** Users can view their order history, including the status of each order.

### Employee Interface

1. **Admin Login:** Employees can log in with their admin credentials to access the admin interface.

2. **Manage Ingredients:** Admins can view and update the inventory of ingredients.

3. **View Orders:** Admins can view all customer orders, including details such as the customer name, ordered products, and production status.

4. **Update Order Status:** Admins can mark orders as finished or unfinished, updating the production status.



## How to Run

1. Ensure you have Python installed on your system.

2. Install the required dependencies:

  *Run the main.py script:
     ```ruby
     python main.py
     ```
   *The application window will open, allowing you to log in or sign up.



## Usage

1. **Login/Signup:**
   - Enter your username and password or sign up with a new username and password.
   - Click the "Login" or "Sign Up" button.

2. **User Interface:**
   - Choose a burger from the menu in the "Order" tab.
   - Enter the quantity and click the "Order" button to place an order.
   - View your order history in the "My Orders" tab.

3. **Employee Interface:**
   - Log in as an admin with the provided credentials.
   - View and manage ingredients in the "Ingredients" tab.
   - View all customer orders in the "Orders" tab.
   - Update order status by selecting an order and clicking the "Declare Order finished/Unfinished" button.

4. **Logout:**
   - Click the "Logout" button to log out of the current session.
  

  ## Notes

- The application uses an SQLite database (`Foundation.db`) to store user data, burger information, orders, and ingredients.

- The application has a dark-themed appearance for a modern and visually appealing interface. 

