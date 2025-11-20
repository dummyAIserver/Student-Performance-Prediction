import pickle
import numpy as np
import streamlit as st

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Student Final Marks Prediction")

st.write("Enter attendance, assignment score, and internal marks to predict final marks.")

# Input fields
attendance = st.number_input("Attendance", placeholder="Enter attendance (0-100)", min_value=0.0, max_value=100.0, step=0.1)
assignment = st.number_input("Assignment Score", placeholder="Enter assignment marks (0-20)", min_value=0.0, max_value=20.0, step=0.1)
internal = st.number_input("Internal Marks", placeholder="Enter internal marks (0-30)", min_value=0.0, max_value=30.0, step=0.1)

if st.button("Predict Final Marks"):
    # Prepare input data
    input_data = np.array([[attendance, assignment, internal]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Final Marks: {prediction:.2f}")
