import streamlit as st
import joblib

# 1. Load the trained model
# @st.cache_resource speeds up the app by loading the model only once
@st.cache_resource
def load_model():
    try:
        return joblib.load('amazon_sentiment_model.joblib')
    except FileNotFoundError:
        return None

pipeline = load_model()

# 2. App Title and Description
st.title("🛒 Amazon Review Sentiment Analyzer")
st.write("Enter a product review below to see if it's Positive or Negative.")

# 3. Text Input
user_input = st.text_area("Type your review here:", height=150)

# 4. Prediction Logic
if st.button("Analyze Sentiment"):
    if pipeline is None:
        st.error("Error: Could not find 'amazon_sentiment_model.joblib'. Please make sure the model file is in the same directory.")
    elif not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        # Make prediction
        prediction = pipeline.predict([user_input])[0]
        probability = pipeline.predict_proba([user_input])[0]
        
        # Determine sentiment and confidence
        sentiment = "Positive" if prediction == 1 else "Negative"
        confidence = probability[1] if prediction == 1 else probability[0]
        
        # Display Results
        st.subheader("Result:")
        if sentiment == "Positive":
            st.success(f"**{sentiment}** (Confidence: {confidence:.2%})")
            st.balloons()
        else:
            st.error(f"**{sentiment}** (Confidence: {confidence:.2%})")