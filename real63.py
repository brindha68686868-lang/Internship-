import time
from datetime import datetime

notifications = [
    "New user registered!",
    "New message received!",
    "Payment completed!",
    "System update available!",
    "Backup completed successfully!"
]

print("=== Real-Time Notification System ===\n")

for notification in notifications:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] 🔔 {notification}")
    time.sleep(3)  # Wait 3 seconds before next notification

print("\nAll notifications delivered!")