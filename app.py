import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load pre-trained model and vectorizer
model = joblib.load("naive_bayes_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load dataset (for charts only)
df = pd.read_csv("complaints_1000.csv")

# Streamlit UI
st.title("Auto Rickshaw Fare Dispute Analyzer")

complaint = st.text_area("Enter your complaint:")

if st.button("Analyze"):
    complaint_vec = vectorizer.transform([complaint])
    prediction = model.predict(complaint_vec)[0]
    st.write("Classification:", prediction)

# Analytics / Charts
st.subheader("Complaint Category Distribution")
if st.checkbox("Show Complaint Distribution"):
    counts = df['Category'].value_counts()

    # Bar chart
    st.bar_chart(counts)

    # Pie chart
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")  # Equal aspect ratio ensures pie is circular
    st.pyplot(fig)

    # Show raw counts
    st.write("Category counts:", counts.to_dict())
