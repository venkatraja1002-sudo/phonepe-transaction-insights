import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# ======================================
# Page setup
# ======================================
st.set_page_config(page_title="PhonePe Transaction Insights", layout="wide")
st.title("📊 PhonePe Transaction Insights Dashboard")

# ======================================
# DB connection
# ======================================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Venkat@123",
    database="phonepe"
)

# ======================================
# Utility
# ======================================
def run_query(query):
    return pd.read_sql(query, conn)

# ======================================
# Sidebar filters
# ======================================
st.sidebar.header("Filters")

year_df = run_query("SELECT DISTINCT year FROM aggregated_transaction ORDER BY year")
quarter_df = run_query("SELECT DISTINCT quarter FROM aggregated_transaction ORDER BY quarter")

year_list = year_df["year"].tolist()
quarter_list = quarter_df["quarter"].tolist()

selected_year = st.sidebar.selectbox("Select Year", ["All"] + year_list)
selected_quarter = st.sidebar.selectbox("Select Quarter", ["All"] + quarter_list)

menu = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Overview",
        "Payment Categories",
        "State Analysis",
        "District Analysis",
        "Pincode Analysis"
    ]
)

# ======================================
# Filter builder
# ======================================
def build_filter(table_alias=""):
    conditions = []
    prefix = f"{table_alias}." if table_alias else ""

    if selected_year != "All":
        conditions.append(f"{prefix}year = {selected_year}")
    if selected_quarter != "All":
        conditions.append(f"{prefix}quarter = {selected_quarter}")

    if conditions:
        return "WHERE " + " AND ".join(conditions)
    return ""

# ======================================
# Overview
# ======================================
if menu == "Overview":
    st.subheader("Project Overview")

    total_query = f"""
        SELECT
            SUM(transaction_amount) AS total_amount,
            SUM(transaction_count) AS total_count
        FROM aggregated_transaction
        {build_filter()}
    """
    total_df = run_query(total_query)

    c1, c2 = st.columns(2)
    c1.metric("Total Transaction Amount", f"₹ {total_df['total_amount'][0]:,.2f}")
    c2.metric("Total Transaction Count", f"{int(total_df['total_count'][0]):,}")

    st.markdown("### Top 10 States")
    states_query = f"""
        SELECT state, SUM(transaction_amount) AS total_amount
        FROM aggregated_transaction
        {build_filter()}
        GROUP BY state
        ORDER BY total_amount DESC
        LIMIT 10
    """
    states_df = run_query(states_query)
    fig = px.bar(states_df, x="state", y="total_amount", title="Top 10 States by Transaction Amount")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Year-wise Trend")
    year_trend_query = """
        SELECT year, SUM(transaction_amount) AS total_amount
        FROM aggregated_transaction
        GROUP BY year
        ORDER BY year
    """
    trend_df = run_query(year_trend_query)
    fig2 = px.line(trend_df, x="year", y="total_amount", markers=True, title="Year-wise Transaction Trend")
    st.plotly_chart(fig2, use_container_width=True)

# ======================================
# Payment Category Analysis
# ======================================
elif menu == "Payment Categories":
    st.subheader("Payment Category Analysis")

    category_query = f"""
        SELECT transaction_type, SUM(transaction_amount) AS total_amount
        FROM aggregated_transaction
        {build_filter()}
        GROUP BY transaction_type
        ORDER BY total_amount DESC
    """
    category_df = run_query(category_query)

    fig = px.pie(
        category_df,
        names="transaction_type",
        values="total_amount",
        title="Payment Category Share"
    )
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
        category_df,
        x="transaction_type",
        y="total_amount",
        title="Payment Category Total Amount"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(category_df, use_container_width=True)

# ======================================
# State Analysis
# ======================================
elif menu == "State Analysis":
    st.subheader("State Level Analysis")

    state_query = f"""
        SELECT state, SUM(transaction_amount) AS total_amount
        FROM aggregated_transaction
        {build_filter()}
        GROUP BY state
        ORDER BY total_amount DESC
    """
    state_df = run_query(state_query)

    fig = px.bar(
        state_df.head(10),
        x="state",
        y="total_amount",
        title="Top 10 States"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Bubble-style state map with manual centroids
    state_coords = pd.DataFrame([
        ["andaman-&-nicobar-islands", 11.7401, 92.6586],
        ["andhra-pradesh", 15.9129, 79.7400],
        ["arunachal-pradesh", 28.2180, 94.7278],
        ["assam", 26.2006, 92.9376],
        ["bihar", 25.0961, 85.3131],
        ["chandigarh", 30.7333, 76.7794],
        ["chhattisgarh", 21.2787, 81.8661],
        ["dadra-&-nagar-haveli-&-daman-&-diu", 20.1809, 73.0169],
        ["delhi", 28.7041, 77.1025],
        ["goa", 15.2993, 74.1240],
        ["gujarat", 22.2587, 71.1924],
        ["haryana", 29.0588, 76.0856],
        ["himachal-pradesh", 31.1048, 77.1734],
        ["jammu-&-kashmir", 33.7782, 76.5762],
        ["jharkhand", 23.6102, 85.2799],
        ["karnataka", 15.3173, 75.7139],
        ["kerala", 10.8505, 76.2711],
        ["ladakh", 34.1526, 77.5770],
        ["lakshadweep", 10.5667, 72.6417],
        ["madhya-pradesh", 22.9734, 78.6569],
        ["maharashtra", 19.7515, 75.7139],
        ["manipur", 24.6637, 93.9063],
        ["meghalaya", 25.4670, 91.3662],
        ["mizoram", 23.1645, 92.9376],
        ["nagaland", 26.1584, 94.5624],
        ["odisha", 20.9517, 85.0985],
        ["puducherry", 11.9416, 79.8083],
        ["punjab", 31.1471, 75.3412],
        ["rajasthan", 27.0238, 74.2179],
        ["sikkim", 27.5330, 88.5122],
        ["tamil-nadu", 11.1271, 78.6569],
        ["telangana", 18.1124, 79.0193],
        ["tripura", 23.9408, 91.9882],
        ["uttar-pradesh", 26.8467, 80.9462],
        ["uttarakhand", 30.0668, 79.0193],
        ["west-bengal", 22.9868, 87.8550]
    ], columns=["state", "lat", "lon"])

    map_df = pd.merge(state_df, state_coords, on="state", how="left").dropna()

    if not map_df.empty:
        fig_map = px.scatter_geo(
            map_df,
            lat="lat",
            lon="lon",
            size="total_amount",
            hover_name="state",
            hover_data=["total_amount"],
            title="State-wise Transaction Map"
        )
        fig_map.update_geos(
            visible=False,
            showcountries=True,
            countrycolor="Black",
            lataxis_range=[6, 38],
            lonaxis_range=[68, 98]
        )
        st.plotly_chart(fig_map, use_container_width=True)

    st.dataframe(state_df, use_container_width=True)

# ======================================
# District Analysis
# ======================================
elif menu == "District Analysis":
    st.subheader("District Level Analysis")

    district_query = f"""
        SELECT district, state, SUM(transaction_amount) AS total_amount
        FROM map_transaction
        {build_filter()}
        GROUP BY district, state
        ORDER BY total_amount DESC
    """
    district_df = run_query(district_query)

    fig = px.bar(
        district_df.head(10),
        x="district",
        y="total_amount",
        color="state",
        title="Top 10 Districts"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "For a real district map, create a file named district_coords.csv "
        "with columns: district,state,lat,lon"
    )

    try:
        coords_df = pd.read_csv("district_coords.csv")
        district_map_df = pd.merge(district_df, coords_df, on=["district", "state"], how="inner")

        if not district_map_df.empty:
            fig_map = px.scatter_geo(
                district_map_df,
                lat="lat",
                lon="lon",
                size="total_amount",
                hover_name="district",
                color="state",
                title="District-wise Transaction Map"
            )
            fig_map.update_geos(
                visible=False,
                showcountries=True,
                countrycolor="Black",
                lataxis_range=[6, 38],
                lonaxis_range=[68, 98]
            )
            st.plotly_chart(fig_map, use_container_width=True)

    except FileNotFoundError:
        st.warning("district_coords.csv not found. District chart is working, but district map needs coordinates.")

    st.dataframe(district_df, use_container_width=True)

# ======================================
# Pincode Analysis
# ======================================
elif menu == "Pincode Analysis":
    st.subheader("Pincode Level Analysis")

    pincode_query = f"""
        SELECT pincode, state, SUM(transaction_amount) AS total_amount
        FROM top_transaction_pincode
        {build_filter()}
        GROUP BY pincode, state
        ORDER BY total_amount DESC
        LIMIT 20
    """
    pincode_df = run_query(pincode_query)

    fig = px.bar(
        pincode_df,
        x="pincode",
        y="total_amount",
        color="state",
        title="Top 20 Pincodes by Transaction Amount"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(pincode_df, use_container_width=True)

conn.close()