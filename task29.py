# Signup and Login System

users = {}

while True:
    print("\n===== User Management System =====")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        username = input("Create Username: ")

        if username in users:
            print("Username already exists!")
        else:
            password = input("Create Password: ")
            users[username] = password
            print("Signup successful!")

    elif choice == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username in users and users[username] == password:
            print("Login successful!")
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or password!")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")