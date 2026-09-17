import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="StarLinkScope",
    page_icon="🛰",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main page spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Main title */
    h1 {
        font-size: 2.6rem !important;
        font-weight: 700 !important;
        letter-spacing: -1px;
    }

    /* Section headings */
    h2 {
        margin-top: 2rem !important;
        font-weight: 650 !important;
    }

    h3 {
        font-weight: 600 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        padding-top: 1.5rem;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        padding: 0.5rem;
    }

    /* Download button */
    .stDownloadButton button {
        width: 100%;
        font-weight: 600;
    }

    /* Table */
    .table-container {
        width: 100%;
        overflow-x: auto;
        border-radius: 8px;
    }

    .starlink-table {
        width: 100%;
        min-width: 1100px;
        border-collapse: collapse;
        font-size: 13px;
    }

    .starlink-table th {
        text-align: left;
        padding: 12px;
        white-space: nowrap;
        border-bottom: 2px solid #666;
        font-weight: 600;
    }

    .starlink-table td {
        padding: 10px 12px;
        white-space: nowrap;
        border-bottom: 1px solid #444;
    }

    .starlink-table tr:hover {
        background-color: rgba(128, 128, 128, 0.15);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

clean_df = pd.read_csv(
    "data/processed/starlink_clean.csv"
)

clean_df["Epoch"] = pd.to_datetime(
    clean_df["Epoch"]
)


# ============================================================
# HEADER
# ============================================================

st.title("STARLINKSCOPE")

st.subheader(
    "Starlink Satellite Analysis Dashboard"
)

st.write(
    "Explore satellite altitude, inclination, orbit groups, "
    "and other orbital characteristics through interactive analysis."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Filters")

st.sidebar.write(
    "Use the controls below to explore the dataset."
)

st.sidebar.divider()


# Orbit Group

orbit_options = ["All"] + sorted(
    clean_df["Orbit_Group"]
    .dropna()
    .unique()
    .tolist()
)

selected_orbit = st.sidebar.selectbox(
    "Orbit Group",
    orbit_options
)


# Satellite Search

satellite_search = st.sidebar.text_input(
    "Search Satellite",
    placeholder="e.g. STARLINK-1008"
)


# Altitude

min_altitude = float(
    clean_df["Altitude_km"].min()
)

max_altitude = float(
    clean_df["Altitude_km"].max()
)

selected_altitude = st.sidebar.slider(
    "Maximum Altitude (km)",
    min_value=min_altitude,
    max_value=max_altitude,
    value=max_altitude,
    step=1.0
)


# Reset

if st.sidebar.button(
    "Reset Filters",
    width="stretch"
):
    st.rerun()


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = clean_df[
    clean_df["Altitude_km"] <= selected_altitude
].copy()


if selected_orbit != "All":

    filtered_df = filtered_df[
        filtered_df["Orbit_Group"] == selected_orbit
    ].copy()


if satellite_search.strip():

    filtered_df = filtered_df[
        filtered_df["Satellite_Name"]
        .str.contains(
            satellite_search.strip(),
            case=False,
            na=False
        )
    ].copy()


# ============================================================
# SIDEBAR RESULT
# ============================================================

st.sidebar.divider()

st.sidebar.metric(
    "Filtered Satellites",
    f"{len(filtered_df):,}"
)

st.sidebar.caption(
    "Filters update the dashboard automatically."
)


# ============================================================
# EMPTY DATA CHECK
# ============================================================

if filtered_df.empty:

    st.warning(
        "No satellites match the current filters. "
        "Try changing the search, orbit group, or altitude."
    )

    st.stop()


# ============================================================
# CALCULATE METRICS
# ============================================================

filtered_total = len(filtered_df)

filtered_average_altitude = (
    filtered_df["Altitude_km"].mean()
)

filtered_average_inclination = (
    filtered_df["Inclination_deg"].mean()
)

filtered_minimum_altitude = (
    filtered_df["Altitude_km"].min()
)

filtered_maximum_altitude = (
    filtered_df["Altitude_km"].max()
)


# ============================================================
# OVERVIEW
# ============================================================

st.header("Satellite Overview")

st.write(
    "Key statistics for the currently selected satellite data."
)


metric_col1, metric_col2, metric_col3, metric_col4, metric_col5 = (
    st.columns(5)
)


with metric_col1:

    with st.container(border=True):

        st.metric(
            "Satellites",
            f"{filtered_total:,}"
        )


with metric_col2:

    with st.container(border=True):

        st.metric(
            "Avg. Altitude",
            f"{filtered_average_altitude:.2f} km"
        )


with metric_col3:

    with st.container(border=True):

        st.metric(
            "Avg. Inclination",
            f"{filtered_average_inclination:.2f}°"
        )


with metric_col4:

    with st.container(border=True):

        st.metric(
            "Min. Altitude",
            f"{filtered_minimum_altitude:.2f} km"
        )


with metric_col5:

    with st.container(border=True):

        st.metric(
            "Max. Altitude",
            f"{filtered_maximum_altitude:.2f} km"
        )


# ============================================================
# ALTITUDE ANALYSIS
# ============================================================

st.header("Altitude Analysis")

st.write(
    f"The current selection contains {filtered_total:,} satellites "
    f"with an average altitude of "
    f"{filtered_average_altitude:.2f} km. "
    f"The selected satellites range from "
    f"{filtered_minimum_altitude:.2f} km to "
    f"{filtered_maximum_altitude:.2f} km."
)


# ============================================================
# DISTRIBUTION
# ============================================================

st.header("Satellite Distribution")

chart_col1, chart_col2 = st.columns(2)


# ------------------------------------------------------------
# Orbit Chart
# ------------------------------------------------------------

with chart_col1:

    with st.container(border=True):

        st.subheader("Satellites by Orbit Group")

        orbit_counts = (
            filtered_df["Orbit_Group"]
            .value_counts()
            .reset_index()
        )

        orbit_counts.columns = [
            "Orbit_Group",
            "Satellite_Count"
        ]

        fig_orbit = px.bar(
            orbit_counts,
            x="Orbit_Group",
            y="Satellite_Count",
            title="Distribution by Orbit Group",
            labels={
                "Orbit_Group": "Orbit Group",
                "Satellite_Count": "Satellite Count"
            }
        )

        fig_orbit.update_xaxes(
            tickangle=0
        )

        fig_orbit.update_layout(
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            ),
            showlegend=False
        )

        st.plotly_chart(
            fig_orbit,
            width="stretch"
        )


# ------------------------------------------------------------
# Altitude Chart
# ------------------------------------------------------------

with chart_col2:

    with st.container(border=True):

        st.subheader("Satellites by Altitude")

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

        altitude_range = pd.cut(
            filtered_df["Altitude_km"],
            bins=altitude_bins,
            labels=altitude_labels
        )

        altitude_counts = (
            altitude_range
            .value_counts(sort=False)
            .reset_index()
        )

        altitude_counts.columns = [
            "Altitude_Range",
            "Satellite_Count"
        ]

        fig_altitude = px.bar(
            altitude_counts,
            x="Altitude_Range",
            y="Satellite_Count",
            title="Distribution by Altitude",
            labels={
                "Altitude_Range": "Altitude Range",
                "Satellite_Count": "Satellite Count"
            }
        )

        fig_altitude.update_xaxes(
            tickangle=0
        )

        fig_altitude.update_layout(
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            ),
            showlegend=False
        )

        st.plotly_chart(
            fig_altitude,
            width="stretch"
        )


# ============================================================
# SCATTER PLOT
# ============================================================

st.header("Altitude vs Inclination")

st.write(
    "Relationship between satellite altitude "
    "and orbital inclination."
)


with st.container(border=True):

    fig_scatter = px.scatter(
        filtered_df,
        x="Inclination_deg",
        y="Altitude_km",
        title="Satellite Altitude vs Orbital Inclination",
        hover_data=[
            "Satellite_Name",
            "Orbit_Group",
            "Altitude_km",
            "Inclination_deg"
        ],
        labels={
            "Inclination_deg": "Inclination (°)",
            "Altitude_km": "Altitude (km)"
        }
    )

    fig_scatter.update_layout(
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig_scatter,
        width="stretch"
    )


# ============================================================
# KEY FINDINGS
# ============================================================

st.header("Key Findings")

finding_col1, finding_col2 = st.columns(2)


with finding_col1:

    with st.container(border=True):

        st.write("**Inclination Patterns**")

        st.write(
            "The dataset contains several distinct "
            "inclination groups, with major concentrations "
            "around approximately 53°, 70° and 98°."
        )


with finding_col2:

    with st.container(border=True):

        st.write("**Altitude Patterns**")

        st.write(
            "Satellite altitude is not uniformly distributed "
            "and covers a wide range of orbital altitudes."
        )


# ============================================================
# EXPORT
# ============================================================

st.header("Export Data")

st.write(
    "Download the complete dataset matching your current filters."
)


download_df = filtered_df.copy()

download_df["Epoch"] = (
    download_df["Epoch"].astype(str)
)

csv_data = download_df.to_csv(
    index=False
)


st.download_button(
    label="Download Filtered Data",
    data=csv_data,
    file_name="starlink_filtered_data.csv",
    mime="text/csv",
    width="stretch"
)


# ============================================================
# DATA TABLE
# ============================================================

st.header("Satellite Data")

st.write(
    f"Showing the first 20 of {filtered_total:,} "
    "matching satellites."
)


display_df = filtered_df.head(20).copy()


display_df["Latitude"] = (
    display_df["Latitude"].round(2)
)

display_df["Longitude"] = (
    display_df["Longitude"].round(2)
)

display_df["Altitude_km"] = (
    display_df["Altitude_km"].round(2)
)

display_df["Inclination_deg"] = (
    display_df["Inclination_deg"].round(2)
)

display_df["Eccentricity"] = (
    display_df["Eccentricity"].round(6)
)

display_df["Mean_Motion_orbits_per_day"] = (
    display_df[
        "Mean_Motion_orbits_per_day"
    ].round(2)
)

display_df["Epoch"] = (
    display_df["Epoch"]
    .astype(str)
    .str[:19]
)


table_html = display_df.to_html(
    index=False,
    classes="starlink-table",
    border=0
)


st.markdown(
    f"""
    <div class="table-container">
        {table_html}
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "StarLinkScope | Starlink Satellite Data Analysis Project"
)