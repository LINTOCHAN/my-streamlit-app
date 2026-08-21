import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")
st.title("Calculator")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("First number", value=0.0, format="%.6f")
with col2:
    b = st.number_input("Second number", value=0.0, format="%.6f")

operation = st.selectbox(
    "Operation",
    ["Add", "Subtract", "Multiply", "Divide"],
)

if st.button("Calculate"):
    if operation == "Add":
        result = a + b
    elif operation == "Subtract":
        result = a - b
    elif operation == "Multiply":
        result = a * b
    else:
        if b == 0:
            st.error("Cannot divide by zero.")
            st.stop()
        result = a / b

    st.success(f"Result: {result}")
