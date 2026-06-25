# 💳 Credit Card Fraud Detection using Machine Learning & Streamlit

An end-to-end Machine Learning project that detects fraudulent credit card transactions using a trained classification model. The project includes data preprocessing, feature engineering, model training, evaluation, and a user-friendly Streamlit web application for real-time fraud prediction.

---

## 📌 Project Overview

Credit card fraud is one of the major challenges faced by financial institutions. This project leverages Machine Learning to classify transactions as **Fraudulent** or **Legitimate** based on transaction details.

The complete pipeline covers:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Model Serialization
- Streamlit Web Application for Predictions

---

## 🚀 Features

- Interactive Streamlit Web Application
- Real-time Fraud Prediction
- Clean Machine Learning Pipeline
- Automatic Data Preprocessing
- One-Hot Encoding for Categorical Features
- Standard Scaling for Numerical Features
- Model Persistence using Joblib
- Easy-to-use Prediction Interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
ML-Fraud_Detection/
│
├── analysis_model.ipynb        # Data analysis & model training
├── fraud_detection.py          # Streamlit application
├── fraud_detection_model.pkl   # Trained model
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 📊 Dataset

This project uses the **PaySim Synthetic Financial Dataset**, which simulates mobile money transactions for fraud detection research.

> Due to GitHub's file size limitations, the dataset is not included in this repository.
Link-https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download

---

## 📈 Features Used

The trained model uses the following features:

| Feature | Description |
|----------|-------------|
| type | Transaction Type |
| amount | Transaction Amount |
| oldbalanceOrg | Sender Balance Before Transaction |
| newbalanceOrig | Sender Balance After Transaction |
| oldbalanceDest | Receiver Balance Before Transaction |
| newbalanceDest | Receiver Balance After Transaction |

---

## 🤖 Machine Learning Pipeline

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. One-Hot Encoding
6. Standard Scaling
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Save Trained Model
11. Deploy using Streamlit

---

## 📸 Application Preview

> <img width="837" height="846" alt="image" src="https://github.com/user-attachments/assets/5f67d76b-98bc-475f-9430-f1c29a995ead" />


Example:

- Home Page
- Prediction Result
- Fraud Detection Output

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ML-Fraud_Detection.git
```

Move into the project directory

```bash
cd ML-Fraud_Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run fraud_detection.py
```

---

## 💻 Usage

1. Select the transaction type.
2. Enter the transaction details.
3. Click **Predict**.
4. The application predicts whether the transaction is **Fraudulent** or **Legitimate**.

---

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 🔮 Future Improvements

- Docker Containerization
- REST API using FastAPI
- MLflow Experiment Tracking
- CI/CD with GitHub Actions
- Model Monitoring
- Cloud Deployment

---

## 👨‍💻 Author

**Roshan Borkar**

Engineering Student | Machine Learning Enthusiast

GitHub: https://github.com/RoshanBorkar29

---

## ⭐ If you found this project useful, consider giving it a star!
