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

## 🏁 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR-USERNAME/amazon-sentiment-analysis.git](https://github.com/YOUR-USERNAME/amazon-sentiment-analysis.git)
    ```
2.  Install dependencies:
    ```bash
    pip install pandas scikit-learn streamlit joblib seaborn
    ```
3.  Run the App:
    ```bash
    streamlit run app.py
    ```
