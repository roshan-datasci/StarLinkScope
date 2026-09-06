# 🛰️ StarLinkScope

## Starlink Satellite Analysis Dashboard

StarLinkScope is a Data Science project focused on exploring and analyzing Starlink satellite data using Python, Pandas, Matplotlib, Plotly, and Streamlit.

The project was created to understand how satellite orbital data can be cleaned, analyzed, visualized, and presented through an interactive web dashboard.

The current version of StarLinkScope focuses on data analysis and interactive visualization using a Starlink satellite dataset containing thousands of satellite records.

---

## 🌌 Project Overview

Satellites operate in different orbital configurations, with characteristics such as altitude, inclination, eccentricity, latitude, longitude, and orbital motion providing useful information about their positions and orbits.

StarLinkScope takes satellite data and transforms it into an interactive dashboard where users can explore these characteristics without needing to work directly with raw CSV files.

The project follows a complete Data Science workflow:

Raw Satellite Data  
↓  
Data Cleaning  
↓  
Exploratory Data Analysis  
↓  
Statistical Analysis  
↓  
Data Visualization  
↓  
Interactive Dashboard  
↓  
GitHub Portfolio Project

---

## 🎯 Project Objectives

The main objectives of StarLinkScope are:

- Explore a real-world satellite dataset
- Understand the structure of satellite orbital data
- Clean and prepare the dataset for analysis
- Calculate important satellite statistics
- Analyze satellite altitude and inclination
- Identify different orbital groups
- Create meaningful data visualizations
- Build an interactive Streamlit dashboard
- Add interactive satellite filtering
- Present the complete project through GitHub

---

## 📊 Dataset

The dataset used in this project contains information about 7,153 Starlink satellite records.

The dataset includes several orbital and positional characteristics.

### Main Variables

| Variable | Description |
|---|---|
| `Satellite_Name` | Name or identifier of the satellite |
| `Epoch` | Time associated with the satellite orbital data |
| `Latitude` | Satellite latitude |
| `Longitude` | Satellite longitude |
| `Altitude_km` | Satellite altitude in kilometers |
| `Inclination_deg` | Orbital inclination in degrees |
| `Eccentricity` | Orbital eccentricity |
| `Mean_Motion_orbits_per_day` | Number of orbital revolutions per day |
| `Orbit_Group` | Derived orbital classification used for analysis |

---

## 🧹 Data Cleaning

Before performing analysis, the dataset was inspected and cleaned using Pandas.

The cleaning process included:

- Checking the dataset dimensions
- Inspecting column names and data types
- Checking for missing values
- Converting the `Epoch` column into datetime format
- Creating derived variables for analysis
- Checking minimum, maximum, mean, and median values
- Saving the cleaned dataset for further analysis

The cleaned dataset is stored inside:

```text
data/processed/
```

The main processed dataset is:

```text
starlink_clean.csv
```

---

## 🔎 Exploratory Data Analysis

Exploratory Data Analysis was performed using Python and Pandas to understand the distribution and characteristics of the satellites.

Some of the main questions explored were:

- How many satellites are present in the dataset?
- What is the average satellite altitude?
- What are the minimum and maximum altitudes?
- What is the average orbital inclination?
- Are there distinct inclination groups?
- How are satellites distributed across altitude ranges?
- What relationship exists between altitude and inclination?

---

## 📈 Key Statistics

Important statistics from the dataset include:

| Metric | Value |
|---|---:|
| Total Satellites | 7,153 |
| Average Altitude | ~505.83 km |
| Median Altitude | ~540.65 km |
| Minimum Altitude | ~172.46 km |
| Maximum Altitude | ~593.59 km |
| Average Inclination | ~51.84° |
| Average Eccentricity | ~0.00016 |

These values provide a general overview of the orbital characteristics represented in the dataset.

---

## 🛰️ Orbit Analysis

The project groups satellites according to their orbital inclination characteristics.

The analysis shows several distinct inclination concentrations.

Major concentrations occur around approximately:

- 53°
- 70°
- 98°

These groups can be explored using the orbit distribution visualization in the dashboard.

The purpose of this analysis is to demonstrate how data analysis and visualization can reveal patterns within satellite datasets.

---

## 📊 Visualizations

StarLinkScope includes several visualizations designed to make the satellite data easier to understand.

### 1. Satellite Distribution by Orbit Group

This visualization shows how many satellites belong to each identified orbit group.

It helps highlight the concentration of satellites across different orbital inclination categories.

### 2. Satellite Distribution by Altitude

The satellites are divided into altitude ranges such as:

- 0–200 km
- 200–300 km
- 300–400 km
- 400–500 km
- 500–600 km

The resulting visualization helps show whether satellite altitudes are evenly distributed or concentrated within particular ranges.

### 3. Altitude vs Inclination

A scatter plot is used to examine the relationship between:

```text
Inclination
     vs
Altitude
```

This visualization makes it easier to identify clusters and patterns within the dataset.

---

## 🔍 Interactive Satellite Filtering

The Streamlit dashboard includes interactive filters that allow users to explore subsets of the dataset.

Users can filter satellites using:

### Orbit Group

Users can select a specific orbital group or view all satellites.

### Maximum Altitude

Users can use an altitude slider to limit the maximum satellite altitude displayed in the filtered results.

The dashboard also displays the number of satellites remaining after applying the selected filters.

This allows users to explore the dataset interactively instead of relying only on static charts.

---

## 🖥️ Dashboard

The project uses Streamlit to transform the Python analysis into an interactive web dashboard.

The dashboard includes:

- Project title and description
- Satellite overview statistics
- Total satellite count
- Average altitude
- Average inclination
- Minimum altitude
- Maximum altitude
- Orbit group visualization
- Altitude distribution
- Altitude vs inclination scatter plot
- Key findings
- Interactive satellite filters
- Satellite data table

---

## 🛠️ Technologies Used

### Python

Used as the primary programming language for data processing, analysis, and application development.

### Pandas

Used for:

- Loading CSV data
- Cleaning data
- Data transformation
- Statistical calculations
- Filtering
- Grouping

### Matplotlib

Used during the exploratory analysis stage to create data visualizations.

### Plotly

Used to create interactive charts for the Streamlit dashboard.

### Streamlit

Used to build the interactive web dashboard.

### Jupyter Notebook

Used for exploratory data analysis and experimentation.

### Git & GitHub

Used for:

- Version control
- Project organization
- Tracking development progress
- Publishing the project as a portfolio

---

## 📁 Project Structure

```text
StarLinkScope/
│
├── data/
│   ├── raw/
│   │   └── starlink_csv.csv
│   │
│   └── processed/
│       ├── starlink_clean.csv
│       ├── starlink_summary.csv
│       └── orbit_summary.csv
│
├── notebooks/
│   └── 01_explore_starlink.ipynb
│
├── app/
│   └── app.py
│
├── visualizations/
│   ├── altitude_distribution.png
│   ├── orbit_groups.png
│   └── altitude_vs_inclination.png
│
├── screenshots/
│   └── dashboard.png
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📓 Jupyter Notebook

The main notebook is located at:

```text
notebooks/01_explore_starlink.ipynb
```

The notebook contains the exploratory analysis performed during the development of StarLinkScope.

It includes:

- Dataset loading
- Dataset inspection
- Data cleaning
- Statistical analysis
- Orbit grouping
- Data visualization
- Analysis findings
- Processed dataset generation

The notebook represents the analytical foundation of the Streamlit dashboard.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

Clone this repository to your local computer:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then navigate into the project directory:

```bash
cd StarLinkScope
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

After activation, the terminal should show:

```text
(.venv)
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Dashboard

Start the application using:

```bash
streamlit run app/app.py
```

The dashboard will open in your browser.

Usually, the dashboard will be available at:

```text
http://localhost:8501
```

---

## 💡 Key Findings

### 1. Satellite Altitude Is Not Uniformly Distributed

The satellites are distributed across different altitude ranges rather than being evenly spread across the complete altitude range.

### 2. Distinct Inclination Groups Exist

The inclination distribution shows clear concentrations around approximately:

```text
53°
70°
98°
```

### 3. Satellites Cover a Wide Altitude Range

The dataset contains satellites from approximately:

```text
172 km
```

to:

```text
594 km
```

This provides a broad range of orbital altitude values for analysis.

### 4. Altitude and Inclination Show Visible Patterns

The altitude-versus-inclination scatter plot reveals clusters and patterns that can be explored through visualization.

---

## 🎓 What I Learned

Building StarLinkScope helped me practice several important Data Science and software development concepts.

### Data Science

- Loading real-world datasets
- Data cleaning
- Handling datetime data
- Descriptive statistics
- Grouping and aggregation
- Filtering datasets
- Identifying patterns

### Data Visualization

- Creating charts with Matplotlib
- Creating interactive charts with Plotly
- Creating scatter plots
- Choosing meaningful visualizations
- Presenting analytical findings

### Application Development

- Building a Streamlit application
- Creating dashboard layouts
- Adding sidebar controls
- Adding interactive filters
- Displaying data tables and metrics

### Software Development

- Organizing a Python project
- Using virtual environments
- Managing dependencies
- Using Git
- Using GitHub
- Maintaining a project README
- Testing and debugging an application

---

## ⚠️ Current Limitations

The current version of StarLinkScope is primarily a static satellite data analysis project.

It does not currently provide:

- Real-time satellite positions
- Live satellite tracking
- A real-time 3D Earth
- Real-time orbital propagation
- Automatic live dataset updates

The current dashboard analyzes the satellite dataset included with the project.

---

## 🔮 Future Improvements

Future versions of StarLinkScope may include more advanced satellite-tracking capabilities.

Possible improvements include:

### 🛰️ Live Satellite Data

Connect the application to a current satellite data source and automatically retrieve updated orbital information.

### 🌍 Interactive World Map

Display satellite positions on an interactive geographic map.

### 🌎 3D Earth Visualization

Create a 3D visualization showing satellites orbiting around Earth.

### 🔄 Real-Time Tracking

Calculate and display current satellite positions based on updated orbital data.

### 🔎 Advanced Search

Allow users to search for individual satellites by satellite name or identifier.

### 📊 Additional Orbital Analysis

Add more detailed analysis of orbital characteristics and satellite movement.

These features are planned as future extensions rather than part of the current version.

---

## 📌 Project Status

**Current Version: V1 — Completed ✅**

The first version of StarLinkScope includes:

- Data exploration
- Data cleaning
- Statistical analysis
- Data visualization
- Streamlit dashboard
- Interactive filtering
- GitHub project organization

Future versions may expand the project toward live satellite tracking and more advanced visualization.

---

## 👨‍💻 Author

**Roshan T**

Data Science Student / Aspiring Data Scientist

StarLinkScope was created as a learning and portfolio project to practice Python, Data Science, data visualization, dashboard development, and GitHub project management.

---

## ⭐ Conclusion

StarLinkScope demonstrates a complete Data Science workflow starting from raw satellite data and ending with an interactive dashboard.

The project combines:

```text
Python
   +
Pandas
   +
Data Analysis
   +
Matplotlib
   +
Plotly
   +
Streamlit
   +
GitHub
```

into one practical project.

The goal of StarLinkScope is not only to analyze satellite data, but also to demonstrate the process of turning a real-world dataset into a usable and interactive Data Science application.

---

## 🚀 Future Vision

StarLinkScope V1 focuses on understanding satellite data through analysis and visualization.

The long-term goal is to evolve the project toward a more interactive satellite exploration platform, potentially including live satellite data, geographic visualization, and 3D orbital tracking.

**From satellite data → to analysis → to visualization → to an interactive satellite exploration platform.** 🛰️🌍