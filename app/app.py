import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="StarLinkScope",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ STARLINKSCOPE")
st.subheader("Starlink Satellite Analysis")

clean_df = pd.read_csv(
    "data/processed/starlink_clean.csv"
)

clean_df["Epoch"] = pd.to_datetime(clean_df["Epoch"])

total_satellites = len(clean_df)
average_altitude = clean_df["Altitude_km"].mean()
average_inclination = clean_df["Inclination_deg"].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Satellites",
        f"{total_satellites:,}"
    )

with col2:
    st.metric(
        "Average Altitude",
        f"{average_altitude:.2f} km"
    )

with col3:
    st.metric(
        "Average Inclination",
        f"{average_inclination:.2f}°"
    )

st.header("📊 Satellite Data")

st.dataframe(clean_df)