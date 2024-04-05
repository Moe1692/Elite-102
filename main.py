import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'bank_users', password = '')
cursor = connection.cursor()
testQuery = ("SELECT * FROM bank_users")
cursor.execute(testQuery)
for item in cursor:
    print(item)
cursor.close()
connection.close()

def home_page():
    print("-" * 20 + "\n")
    print("Bank System\n")
    print("1. Log In")
    print("2. Sign Up")
    print("\n" + "-" * 20 + "\n")

def user_page():
    print("-" * 20 + "\n")
    print("Welcome, user\n")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("\n" + "-" * 20 + "\n")

def admin_page():
    print("-" * 20 + "\n")
    print("Welcome, admin\n")
    print("1. Modify account attributes")
    print("2. Close account")
    print("\n" + "-" * 20 + "\n")

home_page()
user_page()
admin_page()