
import csv
import os

file_path = "dataset/machine_data.csv"

if not os.path.exists(file_path):
    print("Dataset not found. Run prepare_data.py first.")
else:
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    print("Dataset loaded successfully!")
    print("Total records:", len(rows) - 1)
    print("Columns:", rows[0])
    print("\nFirst 5 records:")

    for row in rows[1:6]:
        print(row)
