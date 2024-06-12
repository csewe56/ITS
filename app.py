import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Integrity Track System", layout="wide")

# App title
st.title("Integrity Track System")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = ["Home", "Report Incident", "Case Management", "Financial Tracking", "Audit Visualization"]
choice = st.sidebar.selectbox("Go to", options)

# Sample data
data = {
    "Departments": ["Health", "Education", "Transport", "Finance", "Agriculture"],
    "Allocated Funds": [200000, 150000, 180000, 210000, 170000],
    "Used Funds": [180000, 130000, 160000, 200000, 150000]
}
df = pd.DataFrame(data)

# Home Page
if choice == "Home":
    st.header("Welcome to the Integrity Track System")
    st.write("This platform aims to enhance transparency and accountability in public administration.")

# Report Incident Page
elif choice == "Report Incident":
    st.header("Report Incident")
    with st.form(key='incident_form'):
        name = st.text_input("Name")
        department = st.selectbox("Department", ["Health", "Education", "Transport", "Finance", "Agriculture"])
        incident = st.text_area("Incident Description")
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            st.success(f"Thank you {name}, your report has been submitted.")

# Case Management Page
elif choice == "Case Management":
    st.header("Case Management")
    st.write("Manage reported incidents and track their progress.")
    st.table(df)

# Financial Tracking Page
elif choice == "Financial Tracking":
    st.header("Financial Tracking")
    st.write("Track the allocation and utilization of public funds.")
    st.bar_chart(df.set_index("Departments"))

# Audit Visualization Page
elif choice == "Audit Visualization":
    st.header("Audit Visualization")
    st.write("Visualize audit findings and investigative outcomes.")
    st.line_chart(df.set_index("Departments"))

# Footer
st.sidebar.write("Developed by:")
st.sidebar.write("[Charles Sewe](https://www.linkedin.com/in/charles-sewe)")

st.sidebar.write("[Project Blog Article](https://docs.google.com/document/d/1F1L9EltYW28vnnULs5z-plJ_VAuMDzupGw3w8vheQEM/edit?usp=sharing)")
st.sidebar.write("[Deployed Site]()")

