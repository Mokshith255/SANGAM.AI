import streamlit as st

st.title("List Sum Calculator")
user_input = st.text_input("Enter numbers separated by commas (e.g., 10, 20, 30):", value="0")

if st.button("Calculate Sum"):
    try:
        numbers = [float(i.strip()) for i in user_input.split(",") if i.strip()]
        total_sum = sum(numbers)

        st.success(f"The total sum of the list is: **{total_sum}**")
    except ValueError:
        st.error("Please enter valid numbers separated by commas.")