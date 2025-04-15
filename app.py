# app.py

import streamlit as st
from Converter import Converter

st.set_page_config(page_title="Advanced Unit Converter", layout="wide")

# Dark/Light Mode toggle
mode = st.sidebar.toggle("🌗 Dark Mode")
bg_color = "#0e1117" if mode else "#ffffff"
text_color = "#ffffff" if mode else "#000000"

# Custom CSS for Background
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-color: {bg_color};
    color: {text_color};
}}
[data-testid="stSidebar"] {{
    background-color: {'#262730' if mode else '#f0f2f6'};
}}
</style>
""", unsafe_allow_html=True)

# Sidebar with Image and Selection
st.sidebar.image("images/Mobile App.jpg", use_container_width =True)
category = st.sidebar.selectbox("🔧 Select Conversion Type", list(Converter.units.keys()))

# Tabs for navigation
home_tab, converter_tab, info_tab = st.tabs(["🏠 Home", "🔄 Converter", "ℹ️ Info"])

# Home Tab
with home_tab:
    st.title("🎉 Advanced Unit Converter")
    st.markdown("""
    Quickly convert units from everyday categories including temperature 🌡️, length 📏, weight ⚖️, currency 💱, and many more.
    **Select a category from the sidebar to get started!**
    """)

# Converter Tab
with converter_tab:
    st.header(f"🔄 {category} Converter")

    units_list = Converter.units[category]

    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox("📥 From Unit:", units_list)
        input_value = st.number_input("🔢 Enter Value:", value=1.0, format="%f")

    with col2:
        to_unit = st.selectbox("📤 To Unit:", units_list)

    if from_unit == to_unit:
        converted_value = input_value
    else:
        converted_value = Converter.convert(category, input_value, from_unit, to_unit)

    st.success(f"✅ {input_value} **{from_unit}** = {round(converted_value, 4)} **{to_unit}**")

# Info Tab
with info_tab:
    st.header("ℹ️ Application Information")
    st.markdown("""
    ### 🚀 **Features**
    - **20+ Conversion categories** (Temperature, Length, Weight, Currency, and more)
    - **Real-time and accurate calculations**
    - **Dark & Light mode toggle**
    - **Easy-to-navigate UI with Sidebar and Tabs**

    ### 🛠️ **Future Improvements**
    - Real-time currency updates via API
    - Voice-based input/output
    - Conversion history saving
    """)

