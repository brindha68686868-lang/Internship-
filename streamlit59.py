import streamlit as st
import pandas as pd

# Title
st.title("Sales Dashboard")

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 150, 180, 170, 210]
}

df = pd.DataFrame(data)

# Show data
st.subheader("Sales Data")
st.dataframe(df)

# Metrics
st.metric("Total Sales", df["Sales"].sum())
st.metric("Average Sales", round(df["Sales"].mean(), 2))

# Line chart
st.subheader("Sales Trend")
st.line_chart(df.set_index("Month"))

# Bar chart
st.subheader("Sales Comparison")
st.bar_chart(df.set_index("Month"))