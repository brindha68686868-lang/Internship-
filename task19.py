# Simple Banking Application

balance = 1000  # Initial balance

while True:
    print("\n===== Banking Application =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))

        if amount > 0:
            balance += amount
            print("Deposit Successful!")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid amount!")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank you for using the Banking Application!")
        break

    else:
        print("Invalid choice! Please enter a valid option.")