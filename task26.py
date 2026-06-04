# CRUD Operations - Student Management System

students = {}

while True:
    print("\n===== CRUD Operations =====")
    print("1. Create Student")
    print("2. Read Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Create
    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")

        students[student_id] = {
            "Name": name,
            "Age": age
        }

        print("Student added successfully!")

    # Read
    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for sid, details in students.items():
                print(f"\nStudent ID: {sid}")
                print(f"Name: {details['Name']}")
                print(f"Age: {details['Age']}")

    # Update
    elif choice == "3":
        student_id = input("Enter Student ID to update: ")

        if student_id in students:
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")

            students[student_id]["Name"] = name
            students[student_id]["Age"] = age

            print("Student updated successfully!")
        else:
            print("Student not found!")

    # Delete
    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        if student_id in students:
            del students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")