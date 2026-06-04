# Student Management System

students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll_no] = name
        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for roll_no, name in students.items():
                print("Roll No:", roll_no, "| Name:", name)
        else:
            print("No student records found.")

    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")
        if roll_no in students:
            print("Student Name:", students[roll_no])
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll_no = input("Enter Roll Number to Delete: ")
        if roll_no in students:
            del students[roll_no]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")