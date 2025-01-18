import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Mapping dictionaries
education_mapping = {
    "Graduate School": 1,
    "University": 2,
    "High School": 3,
    "Others": 4
}
marriage_mapping = {
    "Married": 1,
    "Single": 2,
    "Others": 3
}

# Set page configuration
st.set_page_config(page_title="Credit Card Default Prediction", layout="wide")

# Styling
page_style = """
<style>
body {
    background-color: white;
    color: black;
    font-size: 18px;  /* Increased font size for better readability */
}
section.main > div {
    background: rgba(255, 255, 255, 0.9);  /* Light background with transparency */
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
}
footer {
    color: #bbb;
    font-size: 14px;
    text-align: center;
    padding-top: 10px;
}
footer:after {
    content: "Created by Asmita Chavan";
    display: block;
}
h1 {
    color: black;
    text-align: center;
    font-size: 56px;  /* Increased font size */
    text-shadow: 3px 3px 5px white;  /* White shadow effect */
    transform: perspective(500px) rotateX(10deg);  /* 3D effect */
}
h2, h3, p {
    color: black;
    font-size: 20px;  /* Increased font size for readability */
}
.stRadio > label {
    color: black;
    font-size: 20px;  /* Increased font size */
}
input, select, .stNumberInput input {
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    padding: 12px;
    font-size: 18px;  /* Increased font size for form inputs */
    transition: all 0.3s ease;
}
input:focus, select:focus, .stNumberInput input:focus {
    transform: translateY(-2px);
    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.3);
}
.stButton > button {
    background-color: #28a745;
    color: white;
    border-radius: 10px;
    padding: 15px;
    font-size: 20px;  /* Increased font size for button */
    font-weight: bold;
    border: none;
    cursor: pointer;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
}
.stButton > button:hover {
    background-color: #218838;
}
.title-box {
    background-color: #f0f0f0;  /* Whitish-grey background */
    padding: 25px;
    border-radius: 20px;  /* Rounded corners */
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);  /* Soft shadow */
    text-align: center;
}
</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# Centered Title inside the styled box
st.markdown(
    "<div class='title-box'><h1>Credit Card Defaulter Prediction</h1></div>",
    unsafe_allow_html=True,
)

# Input Section
st.write("## Enter Client Information Below")

# Inputs aligned on the same level
col1, col2 = st.columns(2)
with col1:
    st.write("### Personal Information")
    limit_bal = st.number_input("Limit Balance (in $):", min_value=0, value=50000)
    sex = st.radio("Gender:", ["Male", "Female", "Other"])
    education = st.selectbox("Education Level:", list(education_mapping.keys()))
    marriage = st.selectbox("Marital Status:", list(marriage_mapping.keys()))
    age = st.number_input("Age:", min_value=18, value=30)

with col2:
    st.write("### Payment History")
    pay_status_sept = st.number_input("September Repayment Status:", value=0)
    pay_status_aug = st.number_input("August Repayment Status:", value=0)
    pay_status_jul = st.number_input("July Repayment Status:", value=0)
    pay_status_jun = st.number_input("June Repayment Status:", value=0)
    pay_status_may = st.number_input("May Repayment Status:", value=0)
    pay_status_apr = st.number_input("April Repayment Status:", value=0)

# Bill and Payment Amounts
st.write("## Bill and Payment Amounts")

bill_col1, bill_col2, bill_col3 = st.columns(3)
with bill_col1:
    bill_amt_sept = st.number_input("Bill Amount (September):", value=0)
    bill_amt_aug = st.number_input("Bill Amount (August):", value=0)
with bill_col2:
    bill_amt_jul = st.number_input("Bill Amount (July):", value=0)
    bill_amt_jun = st.number_input("Bill Amount (June):", value=0)
with bill_col3:
    bill_amt_may = st.number_input("Bill Amount (May):", value=0)
    bill_amt_apr = st.number_input("Bill Amount (April):", value=0)

pay_col1, pay_col2, pay_col3 = st.columns(3)
with pay_col1:
    pay_amt_sept = st.number_input("Payment Amount (September):", value=0)
    pay_amt_aug = st.number_input("Payment Amount (August):", value=0)
with pay_col2:
    pay_amt_jul = st.number_input("Payment Amount (July):", value=0)
    pay_amt_jun = st.number_input("Payment Amount (June):", value=0)
with pay_col3:
    pay_amt_may = st.number_input("Payment Amount (May):", value=0)
    pay_amt_apr = st.number_input("Payment Amount (April):", value=0)

# Predict button
if st.button("Predict"):
    # Map inputs
    sex = 1 if sex == "Male" else 2 if sex == "Female" else 3
    education = education_mapping[education]
    marriage = marriage_mapping[marriage]

    # Create DataFrame for the input data
    user_input_data = pd.DataFrame({
        "LIMIT_BAL": [limit_bal],
        "SEX": [sex],
        "EDUCATION": [education],
        "MARRIAGE": [marriage],
        "AGE": [age],
        "PAY_0": [pay_status_sept],
        "PAY_2": [pay_status_aug],
        "PAY_3": [pay_status_jul],
        "PAY_4": [pay_status_jun],
        "PAY_5": [pay_status_may],
        "PAY_6": [pay_status_apr],
        "BILL_AMT1": [bill_amt_sept],
        "BILL_AMT2": [bill_amt_aug],
        "BILL_AMT3": [bill_amt_jul],
        "BILL_AMT4": [bill_amt_jun],
        "BILL_AMT5": [bill_amt_may],
        "BILL_AMT6": [bill_amt_apr],
        "PAY_AMT1": [pay_amt_sept],
        "PAY_AMT2": [pay_amt_aug],
        "PAY_AMT3": [pay_amt_jul],
        "PAY_AMT4": [pay_amt_jun],
        "PAY_AMT5": [pay_amt_may],
        "PAY_AMT6": [pay_amt_apr]
    })

    # Make prediction
    predicted_default = model.predict(user_input_data)

    # Display result
    if predicted_default[0] == 1:
        st.error("The client may default on their credit card payment.")
    else:
        st.success("The client is unlikely to default on their credit card payment.")
