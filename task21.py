# Hotel Booking System

rooms = {
    101: {"type": "Single", "price": 1000, "available": True},
    102: {"type": "Double", "price": 2000, "available": True},
    103: {"type": "Deluxe", "price": 3000, "available": True}
}

bookings = {}

while True:
    print("\n===== Hotel Booking System =====")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. View Bookings")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nAvailable Rooms:")
        for room_no, details in rooms.items():
            status = "Available" if details["available"] else "Booked"
            print(f"Room {room_no} | {details['type']} | Rs.{details['price']} | {status}")

    elif choice == "2":
        room_no = int(input("Enter Room Number: "))

        if room_no in rooms and rooms[room_no]["available"]:
            customer_name = input("Enter Customer Name: ")

            bookings[room_no] = customer_name
            rooms[room_no]["available"] = False

            print("Room booked successfully!")
        else:
            print("Room not available or invalid room number.")

    elif choice == "3":
        room_no = int(input("Enter Room Number to cancel booking: "))

        if room_no in bookings:
            del bookings[room_no]
            rooms[room_no]["available"] = True

            print("Booking cancelled successfully!")
        else:
            print("No booking found for this room.")

    elif choice == "4":
        if not bookings:
            print("No bookings found.")
        else:
            print("\nCurrent Bookings:")
            for room_no, customer in bookings.items():
                print(f"Room {room_no} -> {customer}")

    elif choice == "5":
        print("Thank you for using Hotel Booking System!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")