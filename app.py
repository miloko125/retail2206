import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Kruidvat Promo & Price Advisory",
    layout="wide"
)

st.title("Kruidvat Promo & Price Advisory AI Agent")

uploaded_file = st.file_uploader(
    "Upload Price Advisor Data Pack",
    type=["xlsx"]
)

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.success(f"{len(df)} rows loaded")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Products scanned", len(df))
    col2.metric("Competitors attempted", 13)
    col3.metric("Matches found", 0)
    col4.metric("Alerts", 0)

    st.dataframe(df.head())

else:
    st.info("Upload the workshop Excel file.")
