 
# Sentiment Analysis for Employee Feedback

## Overview
This application provides a simple and efficient way to analyze employee feedback using sentiment analysis. By uploading an Excel file containing feedback data, users can gain insights into the overall sentiment of their team's responses. The app utilizes a pre-trained sentiment analysis model to classify feedback as positive, negative, or neutral, along with confidence scores for each sentiment prediction.

## Features
- **Excel File Upload**: Users can upload an Excel (.xlsx) file that must contain two specific columns: "Name" and "Feedback".
- **Sentiment Analysis**: The application uses a transformer-based model to analyze the sentiment of each feedback entry.
- **Results Display**: Users can view the original feedback alongside its predicted sentiment and corresponding confidence score.
- **Overall Sentiment Summary**: The application calculates and displays the overall sentiment of the feedback (Positive, Negative, or Mixed) based on the distribution of sentiments.
- **Visualizations**: The app generates a bar plot representing the distribution of sentiments, making it easy to visualize team feedback.

## Requirements
To run this application, you need:
- Python 3.x
- Streamlit
- Pandas
- Transformers (from Hugging Face)
- Seaborn
- Matplotlib
- OpenPyXL (for reading Excel files)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
