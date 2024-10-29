import streamlit as st
import pandas as pd
from transformers import pipeline
import seaborn as sns
import matplotlib.pyplot as plt

# Load pre-trained sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis")


# Function to analyze sentiment
def analyze_sentiment(feedback):
    result = sentiment_analysis(feedback)[0]
    return result['label'], result['score']


# Function to process uploaded file and display results
def process_file(uploaded_file):
    # Read Excel file
    df = pd.read_excel(uploaded_file)

    # Check if required columns exist
    if 'Name' not in df.columns or 'Feedback' not in df.columns:
        st.error("Uploaded file must contain 'Name' and 'Feedback' columns.")
        return None

    # Apply sentiment analysis
    df['Sentiment'], df['Confidence'] = zip(*df['Feedback'].apply(analyze_sentiment))

    # Display dataframe
    st.write("### Sentiment Analysis Results")
    st.dataframe(df[['Name', 'Feedback', 'Sentiment', 'Confidence']])

    # Calculate sentiment distribution
    sentiment_counts = df['Sentiment'].value_counts(normalize=True) * 100
    overall_sentiment = "Mixed Sentiment"
    if sentiment_counts.get('POSITIVE', 0) > 70:
        overall_sentiment = "Positive"
    elif sentiment_counts.get('NEGATIVE', 0) > 70:
        overall_sentiment = "Negative"

    st.write(f"### Overall Team Sentiment: {overall_sentiment}")

    # Plot sentiment distribution
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=['#66c2a5', '#fc8d62', '#8da0cb'], ax=ax)
    ax.set_title(f"Team Sentiment Distribution - Overall Sentiment: {overall_sentiment}", fontsize=14, weight='bold')
    ax.set_xlabel("Sentiment Type")
    ax.set_ylabel("Percentage (%)")

    for index, value in enumerate(sentiment_counts.values):
        ax.text(index, value + 1, f"{value:.1f}%", ha='center')
    st.pyplot(fig)


# Streamlit UI
st.title("Sentiment Analysis for Employee Feedback")
st.write("Upload an Excel file (.xlsx) with 'Name' and 'Feedback' columns to analyze the sentiment.")

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file:
    process_file(uploaded_file)
