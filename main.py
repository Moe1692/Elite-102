import mysql.connector, time
from pages import *
connection = mysql.connector.connect(user = 'root', database = 'elite102', password = 'A6&71B!iq')
cursor = connection.cursor()

def query(q):
    cursor.execute(q)
    for item in cursor:
        return item[0]

def login():
    id = 0
    user = input("Enter username: ")
    password = input("Enter password: ")
    id = query(f'SELECT id FROM bank_users WHERE Username = "{user}" AND Password = "{password}"')
    if(id == None):
        retry = input("Account not found.\n\n1. Try again\n\n2. Back to home\n\nEnter corresponding number from the list above: ")
        if(retry == "2"):
            home_page_loop()
        else:
            login()
    else:
        user_page_loop(id)

def sign_up():
    print("-" * 20 + "\n")
    name = input("What's your name? ")
    user = input("\nEnter a username: ")
    password = input("\nEnter your password (8 character minimum): ")
    while(len(password) < 8):
        print("\nPassword too short!")
        password = input("Enter your password (8 character minimum): ")
    cursor.execute(f'INSERT INTO bank_users (Name, Username, Password) VALUES ("{name}", "{user}", "{password}")')
    connection.commit()
    id = query(f'SELECT id FROM bank_users WHERE Username = "{user}" AND Password = "{password}"')
    user_page_loop(id)

def check_balance(id):
    balance = query(f"SELECT Balance from bank_users WHERE id = '{id}'")
    print("\nYour balance is " + str(balance))
    user_page_loop(id)

def deposit(id):
    amt = float(input("Enter amount to deposit: "))
    cursor.execute(f"UPDATE bank_users SET Balance = Balance + {amt} WHERE id = {id}")
    connection.commit()
    balance = str(query(f'SELECT Balance FROM bank_users WHERE id = {id}'))
    print(f"Your new balance is {balance} dollars.")
    user_page_loop(id)

def withdraw(id):
    amt = float(input("Enter amount to withdraw: "))
    cursor.execute(f"UPDATE bank_users SET Balance = Balance - {amt} WHERE id = {id}")
    connection.commit()
    balance = str(query(f'SELECT Balance FROM bank_users WHERE id = {id}'))
    print(f"Your new balance is {balance} dollars.")
    user_page_loop(id)

def user_page_loop(id):
    user_page()
    option = input("Enter corresponding number from the list above: ")
    if(option == "1"):
        check_balance(id)
    if(option == "2"):
        deposit(id)
    if(option == '3'):
        withdraw(id)

def home_page_loop():
    home_page()
    option = input("Enter corresponding number from the list above: ")
    if(option == "1"):
        login()
    if(option == "2"):
        sign_up()

    
home_page_loop()

cursor.close()
connection.close()