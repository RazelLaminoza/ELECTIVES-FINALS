import streamlit as st
import pandas as pd
pip install matplotlib
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
file_path = "Predicted_HIV_Cases_2024_2026.csv"
df = pd.read_csv(file_path)

# Sidebar for navigation
st.sidebar.title("🔍 Navigation")
selected_section = st.sidebar.radio("Go to:", ["📊 Forecast Dashboard", "🌍 3D Visualization"])

# Main UI: Forecast Dashboard
if selected_section == "📊 Forecast Dashboard":
    st.title("📊 HIV Case Forecasting in the Philippines (2024-2026)")
    st.write("Select a region and explore its future predictions.")

    # Dropdown to select a region
    selected_region = st.selectbox("🗺 Choose Region", df["Region"].unique())

    # Filter data for selected region
    region_data = df[df["Region"] == selected_region]

    # Interactive buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📈 Show Data Table"):
            st.write(f"Predicted cases for {selected_region}:")
            st.dataframe(region_data.iloc[:, 1:])

    with col2:
        if st.button("📊 Show Graph"):
            fig, ax = plt.subplots(figsize=(8, 5))
            years = ["2022", "2023", "2024", "2025", "2026"]
            cases = region_data.iloc[:, 1:].values.flatten()

            ax.plot(years, cases, marker='o', linestyle='-', color='blue', label="Predicted Cases")
            ax.set_xlabel("Year")
            ax.set_ylabel("HIV Cases")
            ax.set_title(f"HIV Forecast for {selected_region}")
            ax.legend()
            
            st.pyplot(fig)

# 3D Visualization Section
if selected_section == "🌍 3D Visualization":
    st.title("🌍 3D Forecast of HIV Cases in the Philippines")
    st.write("This visualization represents the trend of HIV cases across different regions from 2022 to 2026.")

    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Extract data for all regions
    years = np.array([2022, 2023, 2024, 2025, 2026])
    regions = df["Region"].values
    X = np.tile(years, len(df))  
    Y = np.repeat(np.arange(len(regions)), len(years))  
    Z = df[["Cases_2022", "Cases_2023", "Cases_2024", "Cases_2025", "Cases_2026"]].values.flatten()  

    dx = np.ones_like(X) * 0.4  
    dy = np.ones_like(Y) * 0.4  
    dz = Z  

    ax.bar3d(X, Y, np.zeros_like(Z), dx, dy, dz, color='royalblue', alpha=0.8)

    ax.set_xticks(years)
    ax.set_xticklabels(years, fontsize=12)
    ax.set_yticks(np.arange(len(regions)))
    ax.set_yticklabels(regions, fontsize=10)

    ax.set_xlabel("Year")
    ax.set_ylabel("Region")
    ax.set_zlabel("HIV Cases")
    ax.set_title("📍 3D Forecast Visualization")

    ax.view_init(elev=30, azim=130)
    
    st.pyplot(fig)

# Footer
st.sidebar.write("🔗 Data sourced from HIV case predictions.")
