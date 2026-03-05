import streamlit as st

st.title("🗳️ Voting Eligibility Checker")
st.write("Enter your age below to see if you can head to the polls.")

age = st.number_input("Enter your age:", min_value=0, value=18)

if st.button("Check Eligibility"):
    if age >= 18:
        st.success(f"You are {age} years old. You are eligible to vote! ")
        st.balloons()
    else:
        st.warning(f"You are only {age}. You are not eligible to vote yet.")