import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Create
    if choice == "1":
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))

        cursor.execute(
            "INSERT INTO students (id, name, age) VALUES (?, ?, ?)",
            (student_id, name, age)
        )
        conn.commit()
        print("Student added successfully!")

    # Read
    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        if records:
            print("\n--- Student Records ---")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
        else:
            print("No records found.")

    # Update
    elif choice == "3":
        student_id = int(input("Enter Student ID to update: "))
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))

        cursor.execute(
            "UPDATE students SET name=?, age=? WHERE id=?",
            (name, age, student_id)
        )
        conn.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    # Delete
    elif choice == "4":
        student_id = int(input("Enter Student ID to delete: "))

        cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )
        conn.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

# Close connection
conn.close()