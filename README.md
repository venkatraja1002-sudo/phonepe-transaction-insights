# phonepe-transaction-insights
End-to-End Data Analytics project using PhonePe Pulse dataset with Python, MySQL, ETL pipeline, SQL analysis, and Streamlit dashboard for business insights.

# 📊 PhonePe Transaction Insights

## 🔍 Project Overview

This project analyzes digital payment transaction data using the PhonePe Pulse dataset.  
The objective is to extract insights from transaction, user, and insurance data to understand payment trends, user engagement, and geographical distribution across India.

The project follows a complete End-to-End Data Analytics Pipeline:

JSON → ETL (Python) → MySQL → SQL Analysis → Streamlit Dashboard → Business Insights

---

## 🎯 Problem Statement

With the increasing usage of digital payment systems, analyzing transaction trends, category performance, and state-wise growth is crucial.  

This project focuses on:

- Aggregated transaction analysis
- State and year-wise growth trends
- Top performing states and payment types
- Insurance transaction insights
- Business recommendation generation

---

## 🛠 Tech Stack Used

- Python
- MySQL
- Streamlit
- Plotly
- Pandas
- ETL (Extract, Transform, Load)

---

## 📂 Project Structure

phonepe_project/
│
├── data/                # Raw JSON dataset (PhonePe Pulse)
├── etl.py               # JSON to MySQL data loader
├── queries.sql          # Business SQL queries
├── app.py               # Streamlit dashboard
├── requirements.txt     # Required libraries
└── README.md            # Project documentation

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository

git clone https://github.com/your-username/phonepe_project.git
cd phonepe_project

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Create MySQL Database

Open MySQL and run:

CREATE DATABASE phonepe;
USE phonepe;

(Create tables using queries.sql)

### Step 4: Run ETL Script

python etl.py

This will load JSON data into MySQL tables.

### Step 5: Run Dashboard

streamlit run app.py

---

## 📊 Key Features

- Top 10 States by Transaction Amount
- Year-wise Transaction Growth
- Quarter-wise Trend Analysis
- Transaction Category Distribution
- Interactive Dashboard Filters
- Business Insight Summary

---

## 📈 Sample Insights

- Maharashtra and Karnataka lead in overall transaction volume.
- Digital payments saw massive growth from 2020 to 2023.
- UPI-based transactions dominate the ecosystem.
- Q4 shows higher transaction patterns compared to other quarters.
- Insurance transactions are steadily growing post-2021.

---

## 🧠 Skills Demonstrated

- Data Extraction from complex JSON structure
- Database Design and SQL Optimization
- ETL Pipeline Development
- Data Visualization & Dashboard Development
- Business Insight Generation
- End-to-End Data Analytics Workflow

---

## 🚀 Business Applications

- Customer segmentation
- Fraud detection pattern analysis
- Regional performance comparison
- Product optimization insights
- Marketing strategy planning

---

## 🏆 Project Outcome

This project demonstrates practical implementation of data engineering, data analysis, and visualization techniques to generate actionable business insights from large-scale digital transaction data.

---

## 📌 Dataset Source

PhonePe Pulse Public Dataset  
GitHub: https://github.com/PhonePe/pulse

---

## 👨‍💻 Author

Venkat Raja C  
