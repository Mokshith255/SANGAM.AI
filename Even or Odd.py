import streamlit as st
# title
st.title("Even or Odd Checker")
# Whole no input
number = st.number_input("Enter a whole number:", step=1, value=0)
# logic:
if st.button("Check Result"):
    if number % 2 == 0:
        st.success(f"The number {number} is Even!")
        st.balloons()
    else:
        st.info(f"The number {number} is Odd!")