import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

x_col = st.selectbox("Select the data for the X-axis",
                     ("GDP", "Happiness", "Generosity"))

y_col = st.selectbox("Select the data for the Y-axis",
                     ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")
x_array = df[x_col.lower()]
y_array = df[y_col.lower()]

st.subheader(f"{x_col} and {y_col}")

figure = px.scatter(x=x_array, y=y_array,
                    labels={"x": x_col, "y": y_col})
st.plotly_chart(figure)
