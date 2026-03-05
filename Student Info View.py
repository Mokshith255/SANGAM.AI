import streamlit as st
import pandas as pd

st.title("Student Information Viewer")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("First 10 Records")
    st.write("Displaying the first 10 rows of the dataset:")
    st.dataframe(df.head(10))
    if st.checkbox("Show Summary Statistics"):
        st.write(df.describe())
else:
    st.info("Please upload a CSV file to see the records.")