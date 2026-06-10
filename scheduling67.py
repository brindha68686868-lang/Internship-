import schedule
import time
from datetime import datetime

def task1():
    print(f"[{datetime.now()}] Backup completed!")

def task2():
    print(f"[{datetime.now()}] Sending notification...")

# Schedule tasks
schedule.every(10).seconds.do(task1)
schedule.every(15).seconds.do(task2)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)