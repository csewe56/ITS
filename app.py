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
options = ["Home", "Report Incident", "Case Management", "Financial Tracking", "Audit Visualization", 
           "Data Analysis", "Quiz Application", "Portfolio Project Idea Bank"]
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
    st.write("This platform enhances transparency and accountability in public administration.")

# Report Incident Page
elif choice == "Report Incident":
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

    # Example SHAP values visualization
    X = df["Allocated Funds (KSh)"].values.reshape(-1, 1)
    shap_values = np.random.rand(len(X), 1)  # Dummy SHAP values
    st.write("### SHAP Values")
    shap.summary_plot(shap_values, X, feature_names=["Allocated Funds (KSh)"])

    # Dataset distribution
    st.write("### Dataset Distribution")
    st.write("Distribution of the Allocated Funds")
    st.hist(X, bins=10)

# Interactive Quiz Application (New Feature)
elif choice == "Quiz Application":
    st.header("Interactive Quiz Application")
    st.write("Test your knowledge with multiple-choice questions.")

    # Example quiz
    question = "Which sector received the highest fund allocation?"
    options = ["Executive", "Judiciary", "Health", "Roads & Transport"]
    answer = st.radio(question, options)

    if answer == "Executive":
        st.success("Correct!")
    else:
        st.error("Wrong answer. Try again.")

# Portfolio Project Idea Bank
elif choice == "Portfolio Project Idea Bank":
    st.header("Portfolio Project Idea Bank")
    st.subheader("Guide for this Project Idea Bank")

    st.write("""
    - **Interactive Quiz Application**:
        - **Tech Stack**: Python (Flask/Django), HTML, CSS
        - **Description**: Create a quiz application with scoring, time limits, and feedback. Reinforce Python and web development.
        - **Milestones**:
            - Auth system/Session management
            - Storage of quiz results under user accounts
            - Responsive application
            - Bonus: Add new quiz sets and expose a REST API for quiz questions
    
    - **Algorithm Visualizer**:
        - **Tech Stack**: JavaScript (React), HTML, CSS
        - **Description**: Visualize sorting algorithms like bubble sort, quicksort, etc. Reinforce algorithm concepts with React.
        - **Milestones**:
            - Users can visualize different algorithms
            - Filter between types of algorithms
            - Bonus: Python, C, and JavaScript implementation
    
    - **Chat Application**:
        - **Tech Stack**: JavaScript (React, Node), WebSocket
        - **Description**: Real-time chat app with WebSocket communication.
        - **Milestones**:
            - Authentication and chat history
            - Profile pictures, bios, room messaging

    - **E-commerce Website**:
        - **Tech Stack**: JavaScript (React, Node), MongoDB
        - **Description**: A simple e-commerce website with cart, order history, and product listings.
        - **Milestones**:
            - User authentication
            - Product listing and shopping cart
            - Responsive UI, Stripe integration for payments

    (More project ideas are included in the idea bank for further exploration.)
    """)

# Footer
st.sidebar.write("Developed by:")
st.sidebar.write("[Charles Sewe](https://www.linkedin.com/in/charles-sewe)")

st.sidebar.write("[Project Blog Article](https://docs.google.com/document/d/1F1L9EltYW28vnnULs5z-plJ_VAuMDzupGw3w8vheQEM/edit?usp=sharing)")
st.sidebar.write("[Deployed Site](https://csewe56-qnvf2ccw3bdesyqxhnfuqd.streamlit.app/)")

