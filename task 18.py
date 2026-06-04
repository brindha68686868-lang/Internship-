# Attendance Management System

attendance = {}

while True:
    print("\n===== Attendance Management System =====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        status = input("Enter Attendance (Present/Absent): ")

        attendance[roll_no] = {
            "Name": name,
            "Status": status
        }

        print("Attendance marked successfully!")

    elif choice == "2":
        if attendance:
            print("\n--- Attendance Records ---")
            for roll_no, details in attendance.items():
                print("Roll No:", roll_no)
                print("Name:", details["Name"])
                print("Status:", details["Status"])
                print("-" * 20)
        else:
            print("No attendance records found.")

    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")

        if roll_no in attendance:
            print("\nStudent Found")
            print("Name:", attendance[roll_no]["Name"])
            print("Status:", attendance[roll_no]["Status"])
        else:
            print("Student not found.")

    elif choice == "4":
        print("Exiting Attendance Management System...")
        break

    else:
        print("Invalid choice! Please enter a valid option.")