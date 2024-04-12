import mysql.connector, time
from pages import *
connection = mysql.connector.connect(user = 'root', database = 'elite102', password = 'A6&71B!iq')
cursor = connection.cursor()
testQuery = ("SELECT Balance FROM bank_users")
cursor.execute(testQuery)
for item in cursor:
    print(item[0])

time.sleep(1)
home_page()
time.sleep(0.5)
option = input("Enter corresponding number from the list above: ")
if(option == "1"):
    user = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute(f"SELECT Name FROM bank_users WHERE Username = '{user}' AND Password = '{password}'")
    for item in cursor:
        print(item[0])


cursor.close()
connection.close()