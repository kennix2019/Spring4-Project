import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My Streamlit App")

st.header("Vehicle Sales Dashboard")

   # Histogram with unique key
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist, key='histogram')

   # Scatter Plot with unique key
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_scatter, key='scatter')

   # Checkbox for Raw Data
if st.checkbox('Show raw data', key='raw'):
       st.write(df)
       

