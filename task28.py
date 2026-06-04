# Login System

correct_username = "admin"
correct_password = "12345"

print("===== Login System =====")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == correct_username and password == correct_password:
    print("Login Successful!")
    print("Welcome,", username)
else:
    print("Invalid Username or Password!")