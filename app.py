# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Real Estate Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/latest_prices.csv")

df = load_data()

st.title("🏨 Real Estate Price Prediction Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
years = st.sidebar.multiselect("Select Years", sorted(df["year"].unique()), default=df["year"].unique())
neighborhoods = st.sidebar.multiselect("Select Neighborhoods", sorted(df["neighborhood"].unique()), default=df["neighborhood"].unique())

filtered_df = df[df["year"].isin(years) & df["neighborhood"].isin(neighborhoods)]

# Scatter plot: Price vs Bedrooms
st.subheader("💲 Price vs Bedrooms")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered_df, x="bedrooms", y="price", hue="neighborhood", ax=ax1)
st.pyplot(fig1)

# Line plot: Price trend over years
st.subheader("📈 Price Trend Over Years")
fig2, ax2 = plt.subplots()
sns.lineplot(data=filtered_df, x="year", y="price", hue="neighborhood", marker="o", ax=ax2)
st.pyplot(fig2)

# Heatmap: Price by Neighborhood and Year
st.subheader("🌍 Average Price Heatmap by Neighborhood and Year")
pivot = filtered_df.pivot_table(index="neighborhood", columns="year", values="price", aggfunc="mean")
fig3, ax3 = plt.subplots(figsize=(12, 6))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

