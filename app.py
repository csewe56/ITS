import streamlit as st
import pandas as pd
import numpy as np
import shap

# Page configuration
st.set_page_config(page_title="Integrity Track System", layout="wide")

# App title
st.title("Integrity Track System")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = ["Home", "Report Incident", "Case Management", "Financial Tracking", "Audit Visualization", "Data Analysis"]
choice = st.sidebar.selectbox("Go to", options)

# Sample data
data = {
    "Sectors": [
        "Executive", "Parliament", "Judiciary", "County governments", "Agriculture", "MSME",
        "Housing & Settlement", "Health", "ICT", "Roads & Transport", "Energy & Petroleum",
        "Education", "Manufacturing", "Security", "Tourism", "Environment"
    ],
    "Allocated Funds (KSh)": [
        2.243e12, 44.6e9, 24.7e9, 400.1e9, 54.6e9, 6.7e9, 92.1e9, 127e9, 16.3e9, 193.4e9,
        69.7e9, 656.6e9, 23.7e9, 377.5e9, 23.7e9, 10.7e9
    ]
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
        department = st.selectbox("Department", data["Sectors"])
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
    st.write("Track the allocation of public funds.")
    st.bar_chart(df.set_index("Sectors"))

# Audit Visualization Page
elif choice == "Audit Visualization":
    st.header("Audit Visualization")
    st.write("Visualize audit findings and investigative outcomes.")
    st.line_chart(df.set_index("Sectors"))

# Data Analysis Page
elif choice == "Data Analysis":
    st.header("Data Analysis")
    st.write("Analyze the sector dataset.")

    # Display the dataset
    st.write("### Sector Dataset")
    st.write(df)
    
    # Number of sectors
    st.write("### Number of Sectors")
    st.write(len(data["Sectors"]))

    # Bar graph presentation of dataset
    st.write("### Bar Graph of Allocated Funds")
    st.bar_chart(df.set_index("Sectors"))

    # Example SHAP values visualization (assuming a model is already trained and shap_values are available)
    # Here we'll use dummy data for demonstration
    X = df["Allocated Funds (KSh)"].values.reshape(-1, 1)
    shap_values = np.random.rand(len(X), 1)  # Dummy SHAP values
    st.write("### SHAP Values")
    shap.summary_plot(shap_values, X, feature_names=["Allocated Funds (KSh)"])

    # Anchors and Chinstrap analysis placeholders (assuming appropriate methods are implemented)
    st.write("### Anchors and Chinstrap Analysis")
    st.write("Anchors and Chinstrap analysis would be implemented here.")

    # Dataset distribution
    st.write("### Dataset Distribution")
    st.write("Distribution of the Allocated Funds")
    st.hist(X, bins=10)

# Footer
st.sidebar.write("Developed by:")
st.sidebar.write("[Charles Sewe](https://www.linkedin.com/in/charles-sewe)")

st.sidebar.write("[Project Blog Article](https://docs.google.com/document/d/1F1L9EltYW28vnnULs5z-plJ_VAuMDzupGw3w8vheQEM/edit?usp=sharing)")
st.sidebar.write("[Deployed Site](https://csewe56-qnvf2ccw3bdesyqxhnfuqd.streamlit.app/)")


