import json

import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from PIL import Image

# Define the FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/predict"


# Function to retrieve possible values for "model_key"
def get_model_keys():
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


# Load GetAround logo
logo = Image.open("getaround_logo.png")

# Streamlit App
st.set_page_config(page_title="Getaround Dashboard", page_icon="🚗", layout="wide")

# Add a custom background color
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #e8f0fe;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display logo at the top
st.image(logo, use_column_width=False, width=200)

st.title("Getaround Data Analysis")


# Load the pricing dataset
pricing_file = "get_around_pricing_project.csv"
pricing_df = pd.read_csv(pricing_file)
pricing_cleaned = pricing_df[
    (pricing_df["mileage"] > 0) & (pricing_df["rental_price_per_day"] > 0)
]


# Load delay dataset
delay_file = "get_around_delay_analysis.xlsx"
delay_df = pd.read_excel(delay_file)
positive_delays = delay_df[delay_df["delay_at_checkout_in_minutes"] > 0]

# User-defined threshold
st.markdown("#### Delay Analysis")
st.write(
    "Move the slider to set the delay threshold and see the number of rentals delayed beyond that threshold:"
)
delay_threshold = st.slider(
    "Select Delay Threshold (Minutes)", min_value=0, max_value=180, step=10, value=60
)

# Count delays above threshold
delays_above_threshold = positive_delays[
    positive_delays["delay_at_checkout_in_minutes"] > delay_threshold
].shape[0]

st.markdown(
    f"There are **{delays_above_threshold}** rentals with delays above **{delay_threshold}** minutes!"
)

# Display the interactive charts
st.markdown("### Data Visualizations")

# Create the price distribution plot
price_dist_fig = px.histogram(
    pricing_cleaned,
    x="rental_price_per_day",
    title="Distribution of Rental Prices",
    nbins=30,
    labels={"rental_price_per_day": "Rental Price per Day"},
    color_discrete_sequence=["#636EFA"],
)

# Create the mileage vs price scatter plot
mileage_price_fig = px.scatter(
    pricing_cleaned,
    x="mileage",
    y="rental_price_per_day",
    title="Rental Price vs Mileage",
    labels={"mileage": "Mileage", "rental_price_per_day": "Rental Price per Day"},
    color_discrete_sequence=["#00CC96"],
)

col_chart1, col_chart2 = st.columns(2)
with col_chart1:
    st.plotly_chart(price_dist_fig, use_container_width=True)
with col_chart2:
    st.plotly_chart(mileage_price_fig, use_container_width=True)

st.title("Car Price Prediction Dashboard")

st.write("Enter car features below to predict the rental price:")

# Layout for inputs
with st.container():
    st.markdown("#### Basic Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        # Combobox for "model_key"
        model_keys = get_model_keys()
        selected_model_key = st.selectbox(
            "Select Model Key", model_keys, key="model_key"
        )

    with col2:
        # Combobox for "fuel"
        fuel_types = get_fuel_types()
        selected_fuel_type = st.selectbox(
            "Select Fuel Type", fuel_types, key="fuel_type"
        )

    with col3:
        # Combobox for "paint_color"
        paint_colors = get_paint_colors()
        selected_paint_color = st.selectbox(
            "Select Paint Color", paint_colors, key="paint_color"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        # Number input for mileage
        mileage = st.number_input("Mileage", min_value=0, step=1, key="mileage")

    with col5:
        # Number input for engine power
        engine_power = st.number_input(
            "Engine Power", min_value=0, step=1, key="engine_power"
        )

    with col6:
        # Combobox for "car_type"
        car_types = get_car_types()
        selected_car_type = st.selectbox("Select Car Type", car_types, key="car_type")

# Checkboxes for boolean features
st.markdown("#### Additional Features")
private_parking_available = st.checkbox("Private Parking Available")
has_gps = st.checkbox("Has GPS")
has_air_conditioning = st.checkbox("Has Air Conditioning")
automatic_car = st.checkbox("Automatic Car")
has_getaround_connect = st.checkbox("Has Getaround Connect")
has_speed_regulator = st.checkbox("Has Speed Regulator")
winter_tires = st.checkbox("Winter Tires")


# Layout for prediction result
prediction_placeholder = st.empty()


# Button to send prediction request
if st.button("Predict", key="predict"):
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
        prediction_placeholder.markdown(f"# {result["prediction"]}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
