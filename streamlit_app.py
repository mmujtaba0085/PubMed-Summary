import streamlit as st
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from transformers import pipeline

# Define preprocessing function
def preprocess_text(text):
  text = text.lower()
  text = ''.join([char for char in text if char.isalnum() or char == ' '])
  stop_words = stopwords.words('english')
  text = ' '.join([word for word in text.split() if word not in stop_words])
  tokens = text.split()
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
  return lemmatized_tokens

# Streamlit App
st.title("PubMed Article Summarization")

# User input for article text
user_text = st.text_area("Enter PubMed article text here:", height=200)

# Button to trigger summarization
if st.button("Summarize"):
  # Preprocess the user input
  preprocessed_text = preprocess_text(user_text)

  # Text Summarization with Transformers (Free to Use)
  summarizer = pipeline("summarization")
  summary = summarizer(preprocessed_text, max_length=1, truncation=True)

  # Display the summary
  st.write("**Summary:**")
  st.write(summary[0]['summary_text'])

# Display information about the app
st.sidebar.title("About")
st.sidebar.text("This is a PubMed article summarization app using transformers library.")
