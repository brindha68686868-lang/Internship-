# Hospital Management System

patients = {}

while True:
    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        disease = input("Enter Disease: ")

        patients[patient_id] = {
            "name": name,
            "age": age,
            "disease": disease
        }

        print("Patient added successfully!")

    elif choice == "2":
        if not patients:
            print("No patient records found.")
        else:
            print("\nPatient Records:")
            for pid, details in patients.items():
                print(f"ID: {pid}")
                print(f"Name: {details['name']}")
                print(f"Age: {details['age']}")
                print(f"Disease: {details['disease']}")
                print("-" * 30)

    elif choice == "3":
        patient_id = input("Enter Patient ID to search: ")

        if patient_id in patients:
            print("\nPatient Found:")
            print("Name:", patients[patient_id]["name"])
            print("Age:", patients[patient_id]["age"])
            print("Disease:", patients[patient_id]["disease"])
        else:
            print("Patient not found!")

    elif choice == "4":
        patient_id = input("Enter Patient ID to update: ")

        if patient_id in patients:
            patients[patient_id]["name"] = input("Enter New Name: ")
            patients[patient_id]["age"] = input("Enter New Age: ")
            patients[patient_id]["disease"] = input("Enter New Disease: ")

            print("Patient record updated successfully!")
        else:
            print("Patient not found!")

    elif choice == "5":
        patient_id = input("Enter Patient ID to delete: ")

        if patient_id in patients:
            del patients[patient_id]
            print("Patient record deleted successfully!")
        else:
            print("Patient not found!")

    elif choice == "6":
        print("Exiting Hospital Management System...")
        break

    else:
        print("Invalid choice! Please try again.")