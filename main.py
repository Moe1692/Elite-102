import mysql.connector, time
from pages import *
connection = mysql.connector.connect(user = 'root', database = 'elite102', password = 'A6&71B!iq')
cursor = connection.cursor()

def query(q):
    cursor.execute(q)
    for item in cursor:
        return item[0]

def login():
    ID = input("Enter id: ")
    PIN = int(input("Enter your pin: "))
    id = query(f'SELECT id FROM bank_users WHERE id = {ID} AND PIN = {PIN}')
    if(id == None):
        retry = input("Account not found.\n\n1. Try again\n\n2. Back to home\n\nEnter corresponding number from the list above: ")
        if(retry == "2"):
            home_page_loop()
        else:
            login()
    else:
        if(query(f'SELECT IsAdmin FROM bank_users WHERE id = {id}') == 1):
            admin_page_loop(id)
        else:
            user_page_loop(id)

def sign_up(ID):
    print("-" * 20 + "\n")
    name = input("New new user's name: ")
    PIN = input("\nEnter a 4-digit pin: ")
    while(len(PIN) != 4):
        PIN = input("\nEnter a valid 4-digit pin: ")
    cursor.execute(f'INSERT INTO bank_users (Name, PIN) VALUES ("{name}", {int(PIN)})')
    connection.commit()
    id = query(f'SELECT id FROM bank_users WHERE Name = "{name}" AND PIN = {PIN}')
    print(f"New login id is {id}.")
    admin_page_loop(ID)

def check_balance(id):
    balance = query(f"SELECT Balance from bank_users WHERE id = {id}")
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

def modify(id):
    ID = int(input("Id of user to modify? "))
    edit = input("Edit Name or PIN? ")
    if(edit == "Name"):
        val =  '"' + input("Enter new name: ") + '"'
    if(edit == "PIN"):
        val = int(input("Enter new 4 digit Pin: "))
    cursor.execute(f"UPDATE bank_users SET {edit} = {val} WHERE id = {ID}")
    connection.commit()
    print(f"{edit} has been updated.")
    admin_page_loop(id)

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

def admin_page_loop(id):
    admin_page()
    option = input("Enter corresponding number from the list above: ")
    if(option == "1"):
        sign_up(id)
    if(option == "2"):
        modify(id)

home_page_loop()

cursor.close()
connection.close()