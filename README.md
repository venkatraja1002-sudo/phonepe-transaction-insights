Live demo https://phonepe-transaction-insights-bemzkdjkq5tiytindwmfcu.streamlit.app/

# 📊 PhonePe Transaction Insights Dashboard

This project analyzes **PhonePe digital payment transactions across India** using transaction data stored in JSON files.  
The data is processed, structured, and visualized through an interactive **Streamlit dashboard**.

The dashboard helps users explore:

- Aggregated payment category values
- State-wise transaction totals
- District-wise transaction totals
- Top-performing states
- Top-performing districts
- Top-performing pin codes
- Year-wise and quarter-wise trends

---

## 🚀 Project Overview

The main objective of this project is to transform raw PhonePe transaction data into meaningful business insights.

This project focuses on:

- Analyzing and visualizing aggregated values of payment categories
- Creating maps for total transaction values at state and district levels
- Identifying top-performing states, districts, and pin codes
- Understanding transaction trends across years and quarters

---

## 🛠️ Technologies Used

- **Python** – data processing and dashboard logic
- **Pandas** – data cleaning and analysis
- **Plotly** – interactive charts and maps
- **Streamlit** – web app dashboard
- **MySQL** – local database storage during development
- **GitHub** – version control and deployment integration

---

## 📂 Project Structure

```bash
phonepe-transaction-insights/
│
├── app.py
├── etl.py
├── queries.sql
├── requirements.txt
├── aggregated_transaction.csv
├── map_transaction.csv
├── top_transaction_pincode.csv
└── README.md

📌 Features
1. Overview Dashboard

Displays total transaction amount
Displays total transaction count
Shows top 10 states
Shows year-wise transaction trend

2. Payment Category Analysis

Analyzes transaction amount by payment category
Displays category distribution using pie chart and bar chart

3. State Analysis

Identifies top-performing states
Displays state-wise transaction amount
Visualizes state-level transaction map

4. District Analysis

Identifies top-performing districts
Displays district-level transaction totals
Supports district-level map visualization

5. Pincode Analysis

Identifies top-performing pin codes
Displays top 20 pin codes by transaction amount

6. Filters

Year filter
Quarter filter

#How the Project Works

The project follows this workflow:

Step 1: Extract
Transaction data is collected from PhonePe JSON files.

Step 2: Transform
The raw JSON data is cleaned and converted into structured tabular format.

Step 3: Load
The structured data is loaded into MySQL during local development.

Step 4: Export
For deployment, the MySQL tables are exported into CSV files:
aggregated_transaction.csv
map_transaction.csv
top_transaction_pincode.csv

Step 5: Visualize
The Streamlit dashboard reads the CSV files and creates interactive charts and maps.

Dataset Tables Used
1. Aggregated Transaction
Contains:
state
year
quarter
transaction_type
transaction_count
transaction_amount

2. Map Transaction
Contains:
state
district
year
quarter
transaction_count
transaction_amount

3. Top Transaction Pincode
Contains:
state
pincode
year
quarter
transaction_count
transaction_amount

This project is deployed using Streamlit Community Cloud.
Deployment Steps
Push project files to GitHub
Open Streamlit Community Cloud
Connect GitHub repository
Select app.py as the main file
Deploy the app

Note:
During deployment, local MySQL cannot be used.
So the deployed version reads data from CSV files instead of connecting to MySQL.

##Using this dashboard, we can identify:
Which states have the highest transaction amount
Which districts contribute the most to digital payments
Which pin codes are top-performing
Which payment category has the highest share
How transaction values change across years and quarters
These insights help understand digital payment adoption patterns across India.

##Dashboard Sections
The dashboard contains the following sections:
Overview
Payment Categories
State Analysis
District Analysis
Pincode Analysis

##Conclusion
This project demonstrates how raw transaction data can be transformed into actionable insights using Python, Pandas, and Streamlit.
It highlights state-level, district-level, and pincode-level digital payment performance in a simple and interactive way.
