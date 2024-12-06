import streamlit as st
import requests
import json

# Define the FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/predict"  # Update with your deployed URL

# Streamlit App
st.title("Car Price Prediction Dashboard")

st.write("Enter car features below to predict the rental price:")

# Input fields for the car features
num_inputs = 11  # Number of features
inputs = []
for i in range(num_inputs):
    value = st.number_input(f"Feature {i+1}", step=0.1)
    inputs.append(value)

# Button to send prediction request
if st.button("Predict"):
    try:
        # Prepare the payload
        payload = {"input": [inputs]}
        headers = {"Content-Type": "application/json"}

        # Send the POST request
        response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted rental price: {result['prediction'][0]}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
