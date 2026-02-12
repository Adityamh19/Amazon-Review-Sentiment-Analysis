# 🛒 Amazon Sentiment Analysis

An end-to-end Machine Learning project that classifies Amazon product reviews as **Positive** or **Negative** using Natural Language Processing (NLP).

## 🚀 Project Overview
This project solves the problem of "Class Imbalance" in customer reviews (where most reviews are 5 stars). By implementing **Oversampling** and **N-Gram Vectorization**, the model can accurately detect negative feedback like *"Terrible quality"* even in a dataset dominated by positive reviews.

## 🛠️ Tech Stack
* **Python:** Core language
* **Scikit-Learn:** Machine Learning (Logistic Regression, TF-IDF)
* **Pandas & Seaborn:** Data Cleaning & Visualization
* **Streamlit:** Web App Deployment

## 📊 Key Features
* **Oversampling:** Balanced the dataset to improve detection of negative reviews.
* **Custom Stop Words:** Removed ambiguous words like "product" and "quality" to reduce bias.
* **Real-Time Inference:** Includes a `app.py` script to test reviews instantly in a web interface.

## 🗺️ Project Pipeline
<img width="271" height="790" alt="Screenshot 2026-02-12 161844" src="https://github.com/user-attachments/assets/ac385339-9365-4511-89a8-aee3e096ab59" />

---

## 🌐 Live Demo
You can try out the live web application here:  
**[Amazon Review Sentiment Analyzer](https://amazon-review-sentiment-analysis-hdmycqhcr4ccu2koqpvskp.streamlit.app/)**

### 💤 Important Note on App Availability
If you are accessing the live demo and the website appears to be "sleeping" or taking a moment to load:
* Please click the **"Yes, get this back up!"** button on the screen.
* This will wake up the server and restore the sentiment analysis tool within a few seconds.

---

## 🏁 How to Run Locally
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR-USERNAME/amazon-sentiment-analysis.git](https://github.com/YOUR-USERNAME/amazon-sentiment-analysis.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the App:
    ```bash
    streamlit run app.py
    ```
