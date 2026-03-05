import streamlit as st

st.title("Student Grading System")
name = st.text_input("Student Name:")
col1, col2, col3 = st.columns(3)
with col1:
    maths = st.number_input("Maths:", min_value=0, max_value=100)
with col2:
    physics = st.number_input("Physics:", min_value=0, max_value=100)
with col3:
    chemistry = st.number_input("Chemistry:", min_value=0, max_value=100)

if st.button("Generate Report"):
    total = maths + physics + chemistry
    if total >= 270:
        grade = "A+"
    elif total >= 240:
        grade = "A"
    elif total >= 210:
        grade = "B"
    elif total >= 180:
        grade = "C"
    elif total >= 150:
        grade = "D"
    else:
        grade = "F"

    st.divider()
    st.subheader(f"Report for {name}")
    st.write(f"Total Marks:{total} / 300")

    if grade == "F":
        st.error(f"Grade: {grade}")
    elif grade == "A":
        st.balloons()
        st.success(f"Grade: {grade}")
    elif grade == "B":
        st.balloons()
        st.success(f"Grade: {grade}")
    else :
        st.success(f"Grade: {grade}")

    if maths<=50:
        st.error("Failed in Maths")
    if physics <= 50:
            st.error("Failed in Physics")
    if chemistry <= 50:
            st.error("Failed in Chemistry")
    if maths==100:
        st.success("Acheived a Centum in Maths")
    if physics==100:
        st.success("Acheived a Centum in Physics")
    if chemistry==100:
        st.success("Acheived a Centum in Chemistry")