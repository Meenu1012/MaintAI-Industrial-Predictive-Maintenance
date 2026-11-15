
import joblib
from pathlib import Path
import warnings

MODEL_PATH = (
    Path(__file__).parent.parent
    / "models"
    / "maintai_model_candidate.pkl"
)

model = joblib.load(MODEL_PATH)

FEATURE_NAMES = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]


def predict_machine_failure(
    air_temperature,
    process_temperature,
    rotational_speed,
    torque,
    tool_wear
):
    values = [[
        air_temperature,
        process_temperature,
        rotational_speed,
        torque,
        tool_wear
    ]]

    # Supply the feature names expected by the trained model
    import pandas as pd
    input_data = pd.DataFrame(values, columns=FEATURE_NAMES)

    probabilities = model.predict_proba(input_data)[0]
    failure_index = list(model.classes_).index(1)

    failure_probability = float(
        probabilities[failure_index] * 100
    )

    prediction = int(failure_probability >= 30)

    return {
        "prediction": prediction,
        "failure_vote_percentage": round(failure_probability, 2),
        "status": "Failure Risk" if prediction == 1 else "Normal"
    }


if __name__ == "__main__":
    result = predict_machine_failure(
        air_temperature=298.1,
        process_temperature=308.6,
        rotational_speed=1551,
        torque=42.8,
        tool_wear=0
    )

    print("MaintAI Prediction:")
    print(result)
