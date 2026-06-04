# Library Management System

library = {}

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        library[book_id] = {
            "Title": title,
            "Author": author,
            "Status": "Available"
        }

        print("Book added successfully!")

    elif choice == "2":
        if not library:
            print("No books available.")
        else:
            print("\n--- Book List ---")
            for book_id, details in library.items():
                print(f"\nBook ID: {book_id}")
                print(f"Title: {details['Title']}")
                print(f"Author: {details['Author']}")
                print(f"Status: {details['Status']}")

    elif choice == "3":
        book_id = input("Enter Book ID to search: ")

        if book_id in library:
            details = library[book_id]
            print("\nBook Found!")
            print(f"Title: {details['Title']}")
            print(f"Author: {details['Author']}")
            print(f"Status: {details['Status']}")
        else:
            print("Book not found!")

    elif choice == "4":
        book_id = input("Enter Book ID to issue: ")

        if book_id in library:
            if library[book_id]["Status"] == "Available":
                library[book_id]["Status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
        else:
            print("Book not found!")

    elif choice == "5":
        book_id = input("Enter Book ID to return: ")

        if book_id in library:
            if library[book_id]["Status"] == "Issued":
                library[book_id]["Status"] = "Available"
                print("Book returned successfully!")
            else:
                print("Book is already available.")
        else:
            print("Book not found!")

    elif choice == "6":
        book_id = input("Enter Book ID to delete: ")

        if book_id in library:
            del library[book_id]
            print("Book deleted successfully!")
        else:
            print("Book not found!")

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")