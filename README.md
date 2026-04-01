 **Overview**
This project applies Natural Language Processing (NLP) and the Naïve Bayes model to classify auto rickshaw fare complaints into three categories:
* Overcharge
* Meter Issue
* Route Dispute

*The system is trained on a synthetic dataset of 1000 balanced complaints and deployed as a Streamlit web application. Users can enter complaints, receive instant classification, and view analytics through bar and pie charts.*

**Features:**
* Real‑time complaint classification using a trained Naïve Bayes model
* Model persistence with joblib (no retraining required)
* Interactive analytics (bar chart + pie chart) of complaint distribution
* Simple and lightweight Streamlit interface

**Tech Stack**
* Python 3.9+
* Scikit‑learn (Naïve Bayes, CountVectorizer)
* Pandas (data handling)
* Joblib (model persistence)
* Streamlit (web app framework)
* Matplotlib (visualizations)

**Repository Structure**
Auto-Rickshaw-Fare-Dispute-Analyser/
│── app.py                  # Streamlit application
│── complaints_1000.csv     # Synthetic dataset
│── naive_bayes_model.pkl   # Saved model
│── vectorizer.pkl          # Saved vectorizer
│── requirements.txt        # Dependencies
│── README.md               # Project documentation

**Installation**
*Clone the repository and install dependencies:*

<git clone https://github.com/Jeffwry18/Auto-Rickshaw-Fare-Dispute-Analyser.git
cd Auto-Rickshaw-Fare-Dispute-Analyser
pip install -r requirements.txt>

**Usage**
*Run the Streamlit app locally*
<streamlit run app.py>

**Deployment**
*The app can be deployed on Streamlit Cloud*
1) Push this repository to GitHub.
2) Go to streamlit.io → Sign in → Deploy App.
3) Select app.py as the entry point.
4) Streamlit Cloud will build and host your app.
*You’ll get a public link like*
<https://auto-rickshaw-fare-dispute-analyser.streamlit.app>

**Example Output**
* **Complaint Input:** “Driver charged Rs.500 for a 5 km trip.”
* **Classification:** Overcharge
* **Charts:** Balanced distribution of categories displayed as bar and pie charts.

**Research Context**
This project demonstrates the practical application of NLP and machine learning in transport grievance handling. Inspired by prior work on forum message classification, it adapts the Naïve Bayes model for short complaint texts and integrates visualization for analytical insights.

**References**
* *Scikit‑learn Documentation*
* *Streamlit Documentation*
* *Do Phuc & Nguyen Thi Kim Phung (2007). Using Naïve Bayes Model and NLP for Classifying Messages on Online Forum. IEEE*

**Click the below link to open the app**
<autorickshawfaredisputer.streamlit.app>



