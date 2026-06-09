from openpyxl import Workbook

# Create workbook
wb = Workbook()

# Select active sheet
ws = wb.active
ws.title = "Students"

# Add headers
ws.append(["ID", "Name", "Marks"])

# Add data
students = [
    [1, "John", 90],
    [2, "Alice", 85],
    [3, "Bob", 95],
    [4, "David", 88]
]

for student in students:
    ws.append(student)

# Save Excel file
wb.save("students.xlsx")

print("Excel file created successfully!")