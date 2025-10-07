# Ola-ride-insights
Project Overview

This project is a comprehensive analysis of ride-sharing data from Ola, a leading mobility platform. The primary goal is to extract actionable insights from the raw data to help improve business operations, enhance customer satisfaction, and drive strategic decisions. The project follows a complete data analytics workflow, from cleaning the data to presenting the final insights in an interactive web application.

Key Features
The project is broken down into four main components:

1. Data Cleaning and Preprocessing
Data Loading: The initial dataset was loaded and inspected using Python's Pandas library.

Handling Missing Values: Identified and handled contextual missing data. For example, NaN values in Canceled_Rides_by_Driver were filled with "Not Canceled", and NaN in numerical columns like Driver_Ratings were filled with 0 to represent non-applicable rides.

Data Type Correction: Ensured all columns had the correct data types, especially converting the Date column to a proper datetime format for time-series analysis.

2. SQL Analysis
A temporary in-memory SQLite database was used to run SQL queries directly on the cleaned dataset. Ten key business questions were answered, including:

Total booking value from successful rides (₹35,080,467).

The top 5 most frequent customers.

The primary reasons for ride cancellations by both customers and drivers.

The average ride distance and customer ratings for each vehicle type.

3. Interactive Power BI Dashboard
A 5-page interactive dashboard was built in Power BI to visualize the findings from the analysis. The dashboard is segregated into the following views:

Overall: High-level metrics on ride volume over time and booking status breakdown.

Vehicle Type: Analysis of ride distance and customer ratings by vehicle type.

Revenue: Insights into revenue by payment method and top-spending customers.

Cancellation: A deep dive into the reasons for ride cancellations.

Ratings: Distribution of both driver and customer ratings.

4. Streamlit Web Application
A user-friendly web application was developed using Streamlit to present the project's findings in a clean, accessible interface. The app includes a summary of key insights and showcases the Power BI dashboard pages. Note: Due to admin restrictions on creating public Power BI embed links, the dashboard is presented as a series of high-quality screenshots within the app.

Technologies Used
Programming Language: Python

Data Manipulation: Pandas

Database: SQLite (via sqlite3 Python library)

Dashboarding: Microsoft Power BI

Web Framework: Streamlit

Code Editor: VS Code, Jupyter Notebook

Key Insights Discovered
Significant Revenue: The total revenue from successful rides in the dataset amounted to ₹35,080,467.

Driver Cancellations: The most common reason for drivers canceling rides was "Personal & Car related issue", accounting for over 6,500 cancellations.

Service Reliability Issues: Over 15,900 rides were marked as incomplete due to "Vehicle Breakdown", highlighting a critical area for operational improvement.

High Customer Satisfaction: Customer ratings were consistently high (averaging ~4.0 out of 5) across all vehicle categories, with premium services like 'Prime Plus' and 'Prime Sedan' rated slightly higher.

Short-Distance Preference for Autos: Autos were primarily used for short-distance trips (average of 6.2 km), while all other vehicle types were used for longer trips (average of ~15.5 km).

How to Run This Project
To run the Streamlit application on your local machine, please follow these steps:

Clone the Repository:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

Install Required Libraries:
Make sure you have Python installed. Then, install the necessary libraries using pip.

pip install streamlit pandas Pillow

Run the Streamlit App:
Ensure that the app.py file and the five screenshot files (overall.png, revenue.png, etc.) are in the same directory. These images are required to display the dashboard visuals. Run the following command in your terminal:

streamlit run app.py

Your web browser will automatically open with the application running.

View the Power BI Dashboard:
The .pbix file included in this repository can be opened using Microsoft Power BI Desktop.
