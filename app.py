import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Cleaner Web App", layout="wide")

st.title("📊 Data Cleaner & CSV Analyzer")
st.write("Upload your CSV or Excel file to clean and analyze data easily.")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    st.subheader("Data Summary")
    st.write(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
