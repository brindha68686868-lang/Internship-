import csv

students = [
    ["ID", "Name", "Marks"],
    [1, "John", 90],
    [2, "Alice", 85],
    [3, "Bob", 95],
    [4, "David", 88]
]

with open("students_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for row in students:
        writer.writerow(row)

print("CSV report generated successfully!")