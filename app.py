import streamlit as st
from student_performance_csv import load_data, process_data, top_student

st.title("Student Performance")

# Load
try:
    df = load_data()
except:
    st.error("student_data.csv not found")
    st.stop()

# Process
df = process_data(df)

# Output
st.write(df)

st.write("Top Student")
st.write(top_student(df))
