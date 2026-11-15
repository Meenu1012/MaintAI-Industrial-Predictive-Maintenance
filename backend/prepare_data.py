
import csv
import random
import os

random.seed(42)

os.makedirs("dataset", exist_ok=True)

with open("dataset/machine_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "temperature",
        "vibration",
        "rotational_speed",
        "torque",
        "tool_wear",
        "machine_failure"
    ])

    for _ in range(1000):
        temperature = round(random.uniform(40, 100), 2)
        vibration = round(random.uniform(0.1, 5.0), 2)
        speed = round(random.uniform(1000, 3000), 2)
        torque = round(random.uniform(20, 80), 2)
        wear = round(random.uniform(0, 250), 2)

        failure = int(
            temperature > 85 or
            vibration > 4.0 or
            wear > 220
        )

        writer.writerow([
            temperature, vibration, speed,
            torque, wear, failure
        ])

print("Machine dataset created successfully!")
print("Total records: 1000")
