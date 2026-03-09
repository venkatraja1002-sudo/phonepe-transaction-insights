import streamlit as st
import pandas as pd
import plotly.express as px

# ======================================
# Page setup
# ======================================
st.set_page_config(page_title="PhonePe Transaction Insights", layout="wide")
st.title("📊 PhonePe Transaction Insights Dashboard")

# ======================================
# Load CSV files
# ======================================
@st.cache_data
def load_data():
    aggregated_df = pd.read_csv("aggregated_transaction.csv")
    map_df = pd.read_csv("map_transaction.csv")
    pincode_df = pd.read_csv("top_transaction_pincode.csv")

    # Clean column names
    aggregated_df.columns = aggregated_df.columns.str.strip()
    map_df.columns = map_df.columns.str.strip()
    pincode_df.columns = pincode_df.columns.str.strip()

    return aggregated_df, map_df, pincode_df


aggregated_df, map_df, pincode_df = load_data()

# ======================================
# Sidebar filters
# ======================================
st.sidebar.header("Filters")

year_list = sorted(aggregated_df["year"].dropna().unique().tolist())
quarter_list = sorted(aggregated_df["quarter"].dropna().unique().tolist())

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
# Filter helper
# ======================================
def apply_filters(df):
    filtered_df = df.copy()

    if selected_year != "All" and "year" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["year"] == selected_year]

    if selected_quarter != "All" and "quarter" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["quarter"] == selected_quarter]

    return filtered_df


filtered_aggregated = apply_filters(aggregated_df)
filtered_map = apply_filters(map_df)
filtered_pincode = apply_filters(pincode_df)

# ======================================
# State coordinates for map
# ======================================
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

# ======================================
# Overview
# ======================================
if menu == "Overview":
    st.subheader("Project Overview")

    total_amount = filtered_aggregated["transaction_amount"].sum()
    total_count = filtered_aggregated["transaction_count"].sum()

    c1, c2 = st.columns(2)
    c1.metric("Total Transaction Amount", f"₹ {total_amount:,.2f}")
    c2.metric("Total Transaction Count", f"{int(total_count):,}")

    st.markdown("### Top 10 States")
    states_df = (
        filtered_aggregated.groupby("state", as_index=False)["transaction_amount"]
        .sum()
        .rename(columns={"transaction_amount": "total_amount"})
        .sort_values("total_amount", ascending=False)
        .head(10)
    )

    fig = px.bar(
        states_df,
        x="state",
        y="total_amount",
        title="Top 10 States by Transaction Amount"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Year-wise Trend")
    trend_df = (
        aggregated_df.groupby("year", as_index=False)["transaction_amount"]
        .sum()
        .rename(columns={"transaction_amount": "total_amount"})
        .sort_values("year")
    )

    fig2 = px.line(
        trend_df,
        x="year",
        y="total_amount",
        markers=True,
        title="Year-wise Transaction Trend"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ======================================
# Payment Categories
# ======================================
elif menu == "Payment Categories":
    st.subheader("Payment Category Analysis")

    category_df = (
        filtered_aggregated.groupby("transaction_type", as_index=False)["transaction_amount"]
        .sum()
        .rename(columns={"transaction_amount": "total_amount"})
        .sort_values("total_amount", ascending=False)
    )

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

    state_df = (
        filtered_aggregated.groupby("state", as_index=False)["transaction_amount"]
        .sum()
        .rename(columns={"transaction_amount": "total_amount"})
        .sort_values("total_amount", ascending=False)
    )

    fig = px.bar(
        state_df.head(10),
        x="state",
        y="total_amount",
        title="Top 10 States"
    )
    st.plotly_chart(fig, use_container_width=True)

    map_state_df = pd.merge(state_df, state_coords, on="state", how="left").dropna()

    if not map_state_df.empty:
        fig_map = px.scatter_geo(
            map_state_df,
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

    district_df = (
        filtered_map.groupby(["district", "state"], as_index=False)["transaction_amount"]
        .sum()
        .rename(columns={"transaction_amount": "total_amount"})
        .sort_values("total_amount", ascending=False)
    )

    fig = px.bar(
        district_df.head(10),
        x="district",
        y="total_amount",
        color="state",
        title="Top 10 Districts"
    )
    st.plotly_chart(fig, use_container_width=True)

    try:
        coords_df = pd.read_csv("district_coords.csv")
        coords_df.columns = coords_df.columns.str.strip()

        district_map_df = pd.merge(
            district_df,
            coords_df,
            on=["district", "state"],
            how="inner"
        )

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
        st.warning("district_coords.csv not found. District chart works, but district map needs coordinates.")

    st.dataframe(district_df, use_container_width=True)

# ======================================
# Pincode Analysis
# ======================================
elif menu == "Pincode Analysis":
    st.subheader("Pincode Level Analysis")

    pin_df = (
        filtered_pincode.groupby(["pincode", "state"], as_index=False)["transaction_amount"]
        .sum()
        .rename(columns={"transaction_amount": "total_amount"})
        .sort_values("total_amount", ascending=False)
        .head(20)
    )

    fig = px.bar(
        pin_df,
        x="pincode",
        y="total_amount",
        color="state",
        title="Top 20 Pincodes by Transaction Amount"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(pin_df, use_container_width=True)