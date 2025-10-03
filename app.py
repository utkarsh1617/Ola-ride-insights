import streamlit as st
from PIL import Image

st.set_page_config(page_title="Ola Ride Insights", layout="wide")

st.title("Ola Ride Insights Dashboard")
st.markdown("This application presents a comprehensive analysis of Ola ride data.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Project Summary",
    "Overall Dashboard",
    "Vehicle Type Analysis",
    "Revenue Analysis",
    "Cancellation Analysis",
    "Ratings Analysis"
])

if page == "Project Summary":
    st.header("Project Summary & Key Findings")
    st.markdown("""
    This project analyzes Ola ride-sharing data to derive actionable insights for business improvement.
    The analysis involved data cleaning, SQL querying, and creating an interactive Power BI dashboard.

    **Key SQL Findings:**
    - **Total Successful Rides Revenue:** ₹35,080,467
    - **Most Frequent Customer:** `CID95407` with 15 rides.
    - **Primary Driver Cancellation Reason:** "Personal & Car related issue" (6,542 cases).
    - **Top Incomplete Ride Reason:** "Customer Demand" and "Vehicle Breakdown" were the leading causes.
    - **Customer Satisfaction:** Consistently high across all vehicle types, averaging around a 4.0 rating.
    """)

elif page == "Overall Dashboard":
    st.header("Overall Ride-Sharing Dashboard")
    try:
        image = Image.open('overall.png')
        st.image(image, caption='Overall Ride Metrics', use_container_width=True)
    except FileNotFoundError:
        st.error("Screenshot 'overall.png' not found. Please save it in the correct folder.")

elif page == "Vehicle Type Analysis":
    st.header("Analysis by Vehicle Type")
    try:
        image = Image.open('vehicle_type.png')
        st.image(image, caption='Vehicle Type Metrics', use_container_width=True)
    except FileNotFoundError:
        st.error("Screenshot 'vehicle_type.png' not found. Please save it in the correct folder.")

elif page == "Revenue Analysis":
    st.header("Revenue Insights")
    try:
        image = Image.open('revenue.png')
        st.image(image, caption='Revenue Metrics', use_container_width=True)
    except FileNotFoundError:
        st.error("Screenshot 'revenue.png' not found. Please save it in the correct folder.")

elif page == "Cancellation Analysis":
    st.header("Ride Cancellation Analysis")
    try:
        image = Image.open('cancellation.png')
        st.image(image, caption='Cancellation Metrics', use_container_width=True)
    except FileNotFoundError:
        st.error("Screenshot 'cancellation.png' not found. Please save it in the correct folder.")

elif page == "Ratings Analysis":
    st.header("Driver and Customer Ratings")
    try:
        image = Image.open('ratings.png')
        st.image(image, caption='Ratings Distribution', use_container_width=True)
    except FileNotFoundError:
        st.error("Screenshot 'ratings.png' not found. Please save it in the correct folder.")

