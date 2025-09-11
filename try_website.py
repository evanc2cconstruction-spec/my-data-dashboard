from datetime import date
import streamlit as st
import pandas as pd

df = pd.read_excel('/Users/evansala/Downloads/current_project_summary_2025-09-11.xlsx', sheet_name=3)

st.title("My Data Dashboard")
st.dataframe(df)
st.bar_chart(df['Trade Name'])