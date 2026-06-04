# Inventory Management System

inventory = {}

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))

        inventory[product_id] = {
            "name": product_name,
            "quantity": quantity
        }

        print("Product added successfully!")

    elif choice == "2":
        if inventory:
            print("\nProduct List:")
            for pid, details in inventory.items():
                print(f"ID: {pid}, Name: {details['name']}, Quantity: {details['quantity']}")
        else:
            print("No products available.")

    elif choice == "3":
        product_id = input("Enter Product ID to search: ")

        if product_id in inventory:
            details = inventory[product_id]
            print(f"Product Found - Name: {details['name']}, Quantity: {details['quantity']}")
        else:
            print("Product not found!")

    elif choice == "4":
        product_id = input("Enter Product ID to update: ")

        if product_id in inventory:
            new_quantity = int(input("Enter New Quantity: "))
            inventory[product_id]["quantity"] = new_quantity
            print("Stock updated successfully!")
        else:
            print("Product not found!")

    elif choice == "5":
        product_id = input("Enter Product ID to delete: ")

        if product_id in inventory:
            del inventory[product_id]
            print("Product deleted successfully!")
        else:
            print("Product not found!")

    elif choice == "6":
        print("Exiting Inventory Management System...")
        break

    else:
        print("Invalid choice! Please try again.")