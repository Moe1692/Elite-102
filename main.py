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
    print("4. Modify account attributes")
    print("5. Close account")
    print("\n" + "-" * 20 + "\n")

home_page()
user_page()
admin_page()