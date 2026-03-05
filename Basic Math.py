import streamlit as st
import math
st.title("Basic Math Operations")
st.markdown("Select a program from the sidebar to test the logic.")
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Choose a Program:", [
    "1. Number Comparisons",
    "2. Positive/Negative/Zero",
    "3. Basic Calculator",
    "4. Natural Numbers (Built using For Loop)",
    "5. Natural Numbers (Built using While Loop)",
    "6. Multiplication Table",
    "7. Sum of Digits",
    "8. Factorial Calculator",
    "9. Find Factors",
    "10. Prime Number Checker"
])

st.divider()

if selection == "1. Number Comparisons":
    st.subheader("Compare Two Numbers")
    c1, c2 = st.columns(2)
    a = c1.number_input("First Number", value=0)
    b = c2.number_input("Second Number", value=0)
    if st.button("Compare"):
        if a > b:
            st.success(f"{a} is greater than {b}")
        elif b > a:
            st.success(f"{b} is greater than {a}")
        else:
            st.info("Both numbers are equal.")

elif selection == "2. Positive/Negative/Zero":
    st.subheader("Check Number Sign")
    num = st.number_input("Enter a number:", value=0)
    if num > 0:
        st.success("The number is Positive.")
    elif num < 0:
        st.error("The number is Negative.")
    else:
        st.info("The number is Zero.")

elif selection == "3. Basic Calculator":
    st.subheader("Four-Function Calculator")
    x = st.number_input("Input X")
    y = st.number_input("Input Y")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Addition", x + y)
    col2.metric("Subtraction", x - y)
    col3.metric("Multiplication", x * y)
    if y != 0:
        col4.metric("Division", round(x / y, 2))
    else:
        col4.error("Div by 0")

elif selection == "4. Natural Numbers (Built using For Loop)":
    n = st.number_input("Enter n:", min_value=1, value=1, key="for_n")
    if st.button("Print Numbers"):
        for i in range(1, n + 1):
               st.write(i)

elif selection == "5. Natural Numbers (Built using While Loop)":
    n = st.number_input("Enter n for While Loop:", min_value=1, step=1, key="while_n")
    if st.button("Print Numbers"):
        i = 1
        while i <= n:
            st.write(i)
            i += 1

elif selection == "6. Multiplication Table":
    num_input = st.number_input("Enter a number to see its table:",value=0)
    if st.button("Show Table"):
        st.write(f"### Multiplication Table of {num_input}")
        for i in range(1, 11):
            result = num_input * i
            st.write(f"{num_input} × {i} = **{result}**")

elif selection == "7. Sum of Digits":
    st.subheader("Sum of Digits (While Loop)")
    num = st.number_input("Enter a large number:", min_value=0)
    original = num
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    st.info(f"The sum of the digits in {original} is: **{total}**")

elif selection == "8. Factorial Calculator":
    st.subheader("Factorial Computation")
    n = st.number_input("Enter a number:", min_value=0)
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    st.success(f"{n}! = {fact}")

elif selection == "9. Find Factors":
    st.subheader("Factors of a Number")
    num = st.number_input("Enter number:", min_value=0)
    factors = [i for i in range(1, num + 1) if num % i == 0]
    st.write(f"The factors of {num} are: {factors}")

elif selection == "10. Prime Number Checker":
    st.subheader("Is it a Prime Number?")
    num = st.number_input("Enter number:", min_value=0)
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        st.success(f"✅ {num} is a Prime Number!")
    else:
        st.error(f"❌ {num} is NOT a Prime Number.")