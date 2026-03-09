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
