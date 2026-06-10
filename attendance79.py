import pandas as pd
from datetime import datetime

attendance = []

print("=== AI Attendance System ===")

while True:
    name = input("Enter Student Name (or 'exit'): ")

    if name.lower() == "exit":
        break

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    attendance.append({
        "Name": name,
        "Time": current_time,
        "Status": "Present"
    })

    print(f"{name} marked present!")

# Save attendance
df = pd.DataFrame(attendance)
df.to_csv("attendance.csv", index=False)

print("Attendance saved to attendance.csv")