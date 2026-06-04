# Employee Management System

employees = {}

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        employees[emp_id] = {
            "Name": emp_name,
            "Salary": salary
        }

        print("Employee Added Successfully!")

    elif choice == "2":
        if employees:
            print("\nEmployee Records:")
            for emp_id, details in employees.items():
                print(f"ID: {emp_id}, Name: {details['Name']}, Salary: {details['Salary']}")
        else:
            print("No employee records found.")

    elif choice == "3":
        emp_id = input("Enter Employee ID to Search: ")

        if emp_id in employees:
            print("Employee Details:")
            print("Name:", employees[emp_id]["Name"])
            print("Salary:", employees[emp_id]["Salary"])
        else:
            print("Employee Not Found!")

    elif choice == "4":
        emp_id = input("Enter Employee ID to Delete: ")

        if emp_id in employees:
            del employees[emp_id]
            print("Employee Deleted Successfully!")
        else:
            print("Employee Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")