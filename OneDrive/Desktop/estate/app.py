import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Real Estate Dashboard", layout="wide")

@st.cache_data
def load_data():
    file_path = "data/latest_prices.csv"
    if not os.path.exists(file_path):
        st.error(f"❌ Data file not found: {file_path}")
        st.stop()
    return pd.read_csv(file_path)

df = load_data()

# Add this block just after loading data to debug and check if data is loaded
st.write("### Loaded Data Preview")
st.write(df.head())

if df.empty:
    st.warning("⚠️ The data file is empty!")

st.title("🏨 Real Estate Price Prediction Dashboard")

st.write("### Data Sample")
st.dataframe(df.head())

# Simple plot example
st.write("### Price distribution")
fig, ax = plt.subplots()
sns.histplot(df['price'], bins=30, ax=ax)
st.pyplot(fig)
