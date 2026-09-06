import streamlit as st
import pandas as pd
import plotly.express as px


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
st.subheader("Starlink Satellite Analysis Dashboard")

st.write(
    "Explore satellite altitude, inclination, orbit groups, "
    "and other orbital characteristics through interactive data analysis."
)

# -----------------------------
# Satellite Filters
# -----------------------------

st.sidebar.header("🔍 Satellite Filters")

st.sidebar.write(
    "Use the filters below to explore a subset of the satellite dataset."
)

orbit_options = ["All"] + sorted(
    clean_df["Orbit_Group"].dropna().unique().tolist()
)

selected_orbit = st.sidebar.selectbox(
    "Select Orbit Group",
    orbit_options
)

min_altitude = float(clean_df["Altitude_km"].min())
max_altitude = float(clean_df["Altitude_km"].max())

selected_altitude = st.sidebar.slider(
    "Maximum Altitude (km)",
    min_value=min_altitude,
    max_value=max_altitude,
    value=max_altitude
)

filtered_df = clean_df[
    clean_df["Altitude_km"] <= selected_altitude
]

if selected_orbit != "All":
    filtered_df = filtered_df[
        filtered_df["Orbit_Group"] == selected_orbit
    ]


st.sidebar.metric(
    "Filtered Satellites",
    f"{len(filtered_df):,}"
)

st.divider()

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
st.header("📊 Satellite Overview")

st.write(
    "Key statistics calculated from the Starlink satellite dataset."
)

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
st.divider()

# -----------------------------
# Altitude Analysis
# -----------------------------

st.header("📈 Altitude Analysis")

st.write(
    f"The average satellite altitude is "
    f"{average_altitude:.2f} km."
)


# -----------------------------
# Orbit Group Analysis
# -----------------------------

st.header("📊 Satellite Distribution by Orbit Group")

orbit_counts = clean_df["Orbit_Group"].value_counts().reset_index()

orbit_counts.columns = [
    "Orbit_Group",
    "Satellite_Count"
]

fig_orbit = px.bar(
    orbit_counts,
    x="Orbit_Group",
    y="Satellite_Count",
    title="Satellite Distribution by Orbit Group"
)

fig_orbit.update_xaxes(
    tickangle=0
)

st.plotly_chart(
    fig_orbit,
    use_container_width=True
)


# -----------------------------
# Altitude Distribution
# -----------------------------

st.header("📈 Altitude Distribution")

altitude_bins = [
    0,
    200,
    300,
    400,
    500,
    600
]

altitude_labels = [
    "0–200 km",
    "200–300 km",
    "300–400 km",
    "400–500 km",
    "500–600 km"
]

clean_df["Altitude_Range"] = pd.cut(
    clean_df["Altitude_km"],
    bins=altitude_bins,
    labels=altitude_labels
)

altitude_counts = clean_df["Altitude_Range"].value_counts(
    sort=False
).reset_index()

altitude_counts.columns = [
    "Altitude_Range",
    "Satellite_Count"
]

fig_altitude = px.bar(
    altitude_counts,
    x="Altitude_Range",
    y="Satellite_Count",
    title="Satellite Distribution by Altitude"
)

fig_altitude.update_xaxes(
    tickangle=0
)

st.plotly_chart(
    fig_altitude,
    use_container_width=True
)


# -----------------------------
# Altitude vs Inclination
# -----------------------------

st.header("🔵 Altitude vs Inclination")

st.write(
    "Relationship between satellite altitude and orbital inclination."
)

st.scatter_chart(
    clean_df,
    x="Inclination_deg",
    y="Altitude_km"
)

st.divider()
# -----------------------------
# Key Findings
# -----------------------------

st.header("🔎 Key Findings")


st.write(
    "• Starlink satellites are distributed across several "
    "distinct inclination groups."
)

st.write(
    "• Major inclination concentrations occur around "
    "53°, 70° and 98°."
)

st.write(
    "• Satellite altitude is not uniformly distributed."
)

st.write(
    "• The dataset contains satellites across a wide range "
    "of orbital altitudes."
)

st.divider()
# -----------------------------
# Satellite Data
# -----------------------------

st.header("📋 Satellite Data")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)

st.divider()

st.caption(
    "StarLinkScope — Starlink Satellite Data Analysis Project"
)