import json

import requests
import streamlit as st

# Define the FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/predict"


# Function to retrieve possible values for "model_key"
def get_model_keys():
    # In a real-world scenario, you might fetch this list from an API or a database
    # Example API request (uncomment if applicable):
    # response = requests.get("http://127.0.0.1:8000/model-keys")
    # return response.json() if response.status_code == 200 else []
    return ["Renault", "Peugeot", "Citroen", "BMW", "Mercedes", "Tesla"]


# Function to retrieve possible values for "fuel"
def get_fuel_types():
    return ["diesel", "petrol", "electric", "hybrid"]


# Function to retrieve possible values for "paint_color"
def get_paint_colors():
    return ["black", "white", "blue", "red", "silver", "green"]


# Function to retrieve possible values for "car_type"
def get_car_types():
    return ["sedan", "suv", "coupe", "hatchback", "convertible", "wagon"]


# Streamlit App
st.title("Car Price Prediction Dashboard")

st.write("Enter car features below to predict the rental price:")

# Combobox for "model_key"
model_keys = get_model_keys()
selected_model_key = st.selectbox("Select Model Key", model_keys)

# Combobox for "fuel"
fuel_types = get_fuel_types()
selected_fuel_type = st.selectbox("Select Fuel Type", fuel_types)

# Combobox for "paint_color"
paint_colors = get_paint_colors()
selected_paint_color = st.selectbox("Select Paint Color", paint_colors)

# Combobox for "car_type"
car_types = get_car_types()
selected_car_type = st.selectbox("Select Car Type", car_types)

# Checkboxes for boolean features
private_parking_available = st.checkbox("Private Parking Available")
has_gps = st.checkbox("Has GPS")
has_air_conditioning = st.checkbox("Has Air Conditioning")
automatic_car = st.checkbox("Automatic Car")
has_getaround_connect = st.checkbox("Has Getaround Connect")
has_speed_regulator = st.checkbox("Has Speed Regulator")
winter_tires = st.checkbox("Winter Tires")

# Number inputs for mileage and engine power
mileage = st.number_input("Mileage", min_value=0, step=1)
engine_power = st.number_input("Engine Power", min_value=0, step=1)

# Input fields for the other car features
num_inputs = 7  # Adjusted for remaining features
inputs = []

# Button to send prediction request
if st.button("Predict"):
    # Prepare the payload
    payload = {
        "model_key": selected_model_key,
        "mileage": mileage,
        "engine_power": engine_power,
        "fuel": selected_fuel_type,
        "paint_color": selected_paint_color,
        "car_type": selected_car_type,
        "private_parking_available": private_parking_available,
        "has_gps": has_gps,
        "has_air_conditioning": has_air_conditioning,
        "automatic_car": automatic_car,
        "has_getaround_connect": has_getaround_connect,
        "has_speed_regulator": has_speed_regulator,
        "winter_tires": winter_tires,
    }
    headers = {"Content-Type": "application/json"}

    # Send the POST request
    response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted rental price: {result}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
