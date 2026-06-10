import threading
import time

def task(name):
    for i in range(5):
        print(f"{name} - Count {i+1}")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=task, args=("Thread-1",))
thread2 = threading.Thread(target=task, args=("Thread-2",))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("All threads completed!")