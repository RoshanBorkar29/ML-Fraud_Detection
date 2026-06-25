import logging

import streamlit as st
import pandas as pd
import joblib
from logger import logger

model=joblib.load("fraud_detection_model.pkl")
st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and predict")
st.divider()
transaction_type=st.selectbox("Transaction Type",["CASH_IN","CASH_OUT","DEBIT","PAYMENT","TRANSFER"])

amount=st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input("Old Balance of Origin Account",min_value=0.0,value=10000.0)
newbalanceOrig=st.number_input("New Balance of Origin Account",min_value=0.0,value=9000.0)
oldbalanceDest=st.number_input("Old Balance of Destination Account",min_value=0.0,value=0.0)
newbalanceDest=st.number_input("New Balance of Destination Account",min_value=0.0,value=0.0)


if st.button("Predict"):

    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    logger.info(f"Prediction requested for Amount = {amount}")

    try:

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        logger.info(
            f"Prediction Successful | Prediction = {prediction} | Probability = {probability:.4f}"
        )

        st.subheader(f"Prediction : {int(prediction)}")

        st.metric(
            "Fraud Probability",
            f"{probability*100:.2f}%"
        )

        if prediction == 1:
            st.error("The transaction is Fraudulent")
        else:
            st.success("The transaction is Legitimate")

    except Exception as e:

        logger.error(f"Prediction Failed : {e}")

        st.error("Prediction Failed!")

        st.exception(e)

