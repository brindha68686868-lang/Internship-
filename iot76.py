import random
import time

print("IoT Sensor Started...\n")

while True:
    temperature = round(random.uniform(20, 40), 2)

    print(f"Temperature: {temperature} °C")

    # Simulate sending data to cloud/server
    print("Data sent successfully!\n")

    time.sleep(5)