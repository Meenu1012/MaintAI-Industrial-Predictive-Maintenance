# MaintAI - AI-Powered Industrial Predictive Maintenance System

MaintAI is a machine learning application that predicts potential industrial machine failure risk using five sensor parameters.

## Features
- Random Forest machine learning model
- Flask REST API
- Interactive HTML, CSS and JavaScript dashboard
- Five industrial sensor inputs
- Failure probability and maintenance recommendations
- Input validation
- Prediction history using LocalStorage
- CSV export and history management

## Technology Stack
- Python
- Flask
- Scikit-learn
- Pandas and NumPy
- Joblib
- HTML, CSS and JavaScript

## Dataset
UCI AI4I 2020 Predictive Maintenance Dataset
10,000 synthetic records.

Dataset: https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

## Model Evaluation
5-fold stratified cross-validation:
- Mean Accuracy: 98.30%
- Failure Precision: 77.20%
- Failure Recall: 71.10%
- Failure F1-Score: 73.75%

These metrics are based on the AI4I dataset and do not guarantee real-world industrial performance.

## Installation
1. Clone this repository.
2. Create a virtual environment:
   python -m venv venv
3. Activate it:
   .\venv\Scripts\Activate.ps1
4. Install dependencies:
   pip install -r requirements.txt
5. Start the backend:
   python backend/app.py
6. Open frontend/index.html in your browser.

## API
POST http://127.0.0.1:5000/predict

## Project Structure
- backend/ - Flask API and ML prediction code
- frontend/ - Web dashboard
- models/ - Trained machine learning model
- requirements.txt - Python dependencies

## Important Note
This is a portfolio project using synthetic dataset records. It does not use live industrial sensor data.

## Author
Machine Learning and Full-Stack Development Portfolio Project
