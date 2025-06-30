import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

st.title("Welcome to Age Calculator")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}")

today = datetime.date.today()
st.write(f"Today's date is: {today}")

dob = st.date_input(
    "Enter your Date of Birth",
    value=today,
    min_value=datetime.date(1945, 8, 15),
    max_value=datetime.date(2125, 1, 7)
)

if today >= dob:
    diff = relativedelta(today, dob)
    st.write(f"Your Age: {diff.years} years, {diff.months} months, {diff.days} days")
else:
    st.warning("Date of birth cannot be in the future.")
