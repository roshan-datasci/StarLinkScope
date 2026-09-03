import streamlit as st
import pandas as pd


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="StarLinkScope",
    page_icon="🛰️",
    layout="wide"
)


# -----------------------------
# Load data
# -----------------------------

clean_df = pd.read_csv(
    "data/processed/starlink_clean.csv"
)

clean_df["Epoch"] = pd.to_datetime(clean_df["Epoch"])


# -----------------------------
# Title
# -----------------------------

st.title("🛰️ STARLINKSCOPE")

st.subheader("Starlink Satellite Analysis")

st.write(
    "This dashboard explores satellite altitude, "
    "inclination and orbital characteristics."
)

# -----------------------------
# Calculate metrics
# -----------------------------

total_satellites = len(clean_df)

average_altitude = clean_df["Altitude_km"].mean()

average_inclination = clean_df["Inclination_deg"].mean()

minimum_altitude = clean_df["Altitude_km"].min()

maximum_altitude = clean_df["Altitude_km"].max()


# -----------------------------
# Display metrics
# -----------------------------

col1, col2, col3, col4, col5 = st.columns(5)


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


with col4:
    st.metric(
        "Minimum Altitude",
        f"{minimum_altitude:.2f} km"
    )


with col5:
    st.metric(
        "Maximum Altitude",
        f"{maximum_altitude:.2f} km"
    )

st.header("📈 Altitude Analysis")
st.write(
    f"The average satellite altitude is "
    f"{average_altitude:.2f} km."
)

# -----------------------------
# Orbit Group Analysis
# -----------------------------


st.header("📊 Satellite Distribution by Orbit Group")

orbit_counts = clean_df["Orbit_Group"].value_counts()

st.bar_chart(orbit_counts)


# -----------------------------
# Satellite Data
# -----------------------------

st.header("📋 Satellite Data")

st.dataframe(
    clean_df.head(100),
    use_container_width=True
)