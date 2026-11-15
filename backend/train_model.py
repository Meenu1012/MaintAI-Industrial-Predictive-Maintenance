
import csv
import random
import pickle
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
X = []
y = []

with open("dataset/machine_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        X.append([
            float(row["temperature"]),
            float(row["vibration"]),
            float(row["rotational_speed"]),
            float(row["torque"]),
            float(row["tool_wear"])
        ])
        y.append(int(row["machine_failure"]))

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

print("Model training completed!")
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model
os.makedirs("models", exist_ok=True)

with open("models/maintenance_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")
