import json

import requests
import streamlit as st

# Define the FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/predict"

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
    # Prepare the payload
    payload = {
        "model_key": "Renault",
        "mileage": 77334,
        "engine_power": 256,
        "fuel": "diesel",
        "paint_color": "black",
        "car_type": "coupe",
        "private_parking_available": True,
        "has_gps": False,
        "has_air_conditioning": True,
        "automatic_car": False,
        "has_getaround_connect": False,
        "has_speed_regulator": True,
        "winter_tires": False,
    }
    headers = {"Content-Type": "application/json"}

    # Send the POST request
    response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted rental price: {result}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
