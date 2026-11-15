# MaintAI – AI-Powered Industrial Predictive Maintenance System

MaintAI is a Machine Learning-based web application that predicts potential industrial machine failures using sensor readings.

## Live Project

- **Frontend Website:** https://maintai-frontend.onrender.com
- **Backend API:** https://maintai-industrial-predictive-maintenance.onrender.com
- **GitHub Repository:** https://github.com/Meenu1012/MaintAI-Industrial-Predictive-Maintenance

## Project Objective

The objective of MaintAI is to predict whether an industrial machine may fail or work normally by analyzing its sensor values. It helps identify possible machine problems early and supports timely maintenance.

## Features

- Predicts machine condition as Normal or Failure Risk.
- Accepts five machine sensor readings.
- Uses a Random Forest Machine Learning model.
- Displays failure vote percentage.
- Provides maintenance recommendations.
- Shows prediction statistics on a dashboard.
- Stores prediction history in the browser.
- Supports CSV download of prediction history.
- Validates sensor inputs.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Scikit-learn | Machine Learning model |
| Random Forest | Failure prediction algorithm |
| Pandas | Data handling |
| NumPy | Numerical calculations |
| Flask | Backend API |
| HTML | Webpage structure |
| CSS | Website design |
| JavaScript | Dashboard functionality |
| Joblib | Saving and loading the ML model |
| Git and GitHub | Version control and code hosting |
| Render | Cloud deployment |

## Sensor Inputs

The application uses five sensor parameters:

1. Air Temperature (K)
2. Process Temperature (K)
3. Rotational Speed (rpm)
4. Torque (Nm)
5. Tool Wear (min)

## Dataset

**AI4I 2020 Predictive Maintenance Dataset**

- Contains 10,000 synthetic records.
- Used to train and evaluate the Machine Learning model.

Dataset source:
https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

## Model Evaluation

The Random Forest model was evaluated using 5-fold stratified cross-validation.

| Metric | Result |
|---|---:|
| Mean Accuracy | 98.30% |
| Failure Precision | 77.20% |
| Failure Recall | 71.10% |
| Failure F1-Score | 73.75% |

These results are based on the AI4I dataset and do not guarantee real-world industrial performance.

## Project Outcome

Developed and deployed a complete Machine Learning web application that accepts machine sensor readings, predicts possible failure risks, displays results, and provides maintenance recommendations.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Meenu1012/MaintAI-Industrial-Predictive-Maintenance.git
```

### 2. Open the project folder

```bash
cd MaintAI-Industrial-Predictive-Maintenance
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment (Windows)

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the Flask backend

```bash
python backend/app.py
```

Backend runs locally at:

http://127.0.0.1:5000/

### 7. Open the frontend

Open `frontend/index.html` in your browser.

Note: The frontend is configured to use the deployed Render API by default.

## API Endpoint

**POST**

https://maintai-industrial-predictive-maintenance.onrender.com/predict

The API accepts five sensor values and returns a machine condition prediction.

## Project Structure

```text
MaintAI/
│
├── backend/
│   ├── app.py
│   └── predict.py
│
├── frontend/
│   └── index.html
│
├── models/
│   └── maintai_model_candidate.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Limitations

- Uses the synthetic AI4I 2020 dataset.
- Does not connect to real industrial machines or live sensors.
- Predictions are intended for demonstration and learning purposes.

## Author

Developed as a Machine Learning and Full-Stack Development portfolio project.
