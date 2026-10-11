
import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

# App title
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to estimate its price.")

# Load the saved model
model_path = os.path.join(os.path.dirname(__file__), "house_price_model.pkl")
model = joblib.load(model_path)

# Input fields
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
square_feet = st.number_input("Square Feet", min_value=100, max_value=10000, value=2500)
house_age = st.number_input("House Age (years)", min_value=0, max_value=200, value=5)
location_rating = st.number_input("Location Rating", min_value=1, max_value=5, value=4)

# Prediction button
if st.button("Predict Price"):
    new_house = pd.DataFrame({
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Square Feet": [square_feet],
        "House Age": [house_age],
        "Location Rating": [location_rating]
    })

    predicted_price = model.predict(new_house)[0]

    st.success(f"Predicted House Price: ${predicted_price:,.2f}")