
from flask import Flask, request, jsonify
from predict import predict_machine_failure
import math

app = Flask(__name__)

# Basic sensor input validation ranges
SENSOR_LIMITS = {
    "air_temperature": (250, 350),
    "process_temperature": (250, 400),
    "rotational_speed": (1, 10000),
    "torque": (0, 200),
    "tool_wear": (0, 1000)
}


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to MaintAI",
        "status": "API is running",
        "model": "AI4I 2020 Predictive Maintenance"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        required = list(SENSOR_LIMITS.keys())

        if not isinstance(data, dict):
            return jsonify({
                "error": "Please provide sensor values as JSON"
            }), 400

        if not all(key in data for key in required):
            return jsonify({
                "error": "All five sensor values are required",
                "required_fields": required
            }), 400

        values = []

        for key in required:
            raw_value = data[key]

            if isinstance(raw_value, bool):
                return jsonify({
                    "error": f"{key} must be a numeric value"
                }), 400

            try:
                value = float(raw_value)
            except (ValueError, TypeError):
                return jsonify({
                    "error": f"{key} must be a valid number"
                }), 400

            if not math.isfinite(value):
                return jsonify({
                    "error": f"{key} must be a finite number"
                }), 400

            minimum, maximum = SENSOR_LIMITS[key]

            if not minimum <= value <= maximum:
                return jsonify({
                    "error": f"{key} must be between {minimum} and {maximum}"
                }), 400

            values.append(value)

        result = predict_machine_failure(*values)

        return jsonify(result)

    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({
            "error": "Unable to generate prediction"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
