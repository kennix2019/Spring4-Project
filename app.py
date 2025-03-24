import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My Streamlit App")

st.header("Vehicle Sales Dashboard")

st.text("This project aims to provide you with additional practice on common software engineering tasks.")
st.text("These tasks will augment and complement your data skills, and make you a more attractive job candidate to potential employers.")

df = pd.read_csv('vehicles_us.csv')

   # Histogram with unique key
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist, key='histogram')

   # Scatter Plot with unique key
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_scatter, key='scatter')

   # Checkbox for Raw Data
if st.checkbox('Show raw data', key='raw'):
       st.write(df)
       
fig = px.scatter(df, x='model_year', y='price', title='All Data Sample')
st.plotly_chart(fig)
 
