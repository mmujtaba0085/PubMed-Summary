PubMed Article Summarization with Streamlit
This project utilizes Streamlit to create a web application for summarizing PubMed articles. Users can input text or upload articles, and the application provides a concise summary using rule-based summarization techniques.
Data Preprocessing
The application performs basic text preprocessing on the input text:
1.	Lowercasing: Converts all characters to lowercase.
2.	Alphanumeric filtering: Removes non-alphanumeric characters except spaces.
3.	Stop word removal: Eliminates common English stop words using NLTK.
4.	Lemmatization: Reduces words to their base form using WordNetLemmatizer from NLTK.
Streamlit Application
The Streamlit app offers the following functionalities:
•	Title: "PubMed Article Summarization"
•	Text Input: Users can paste PubMed article text in a text area.
•	Summarization Button: Clicking the "Summarize" button triggers the summarization process.(Not working)
•	Summary Display: The application displays the original article text alongside the generated summary.(not WOrking)
•	About Section: The sidebar provides a short description of the app's purpose.
Code Breakdown
The core functionalities are implemented in streamlit_app.py:
•	Imports:
o	streamlit as st: Enables Streamlit app development.
o	WordNetLemmatizer and stopwords from nltk: Used for text preprocessing.
o	pipeline from transformers: Provides access to the summarization pipeline.
•	preprocess_text function: Performs the text cleaning steps mentioned earlier.
•	Streamlit App Definition:
o	Sets the app title.
o	Creates a text area for user input.
o	Defines a button for triggering summarization.
o	Within the button click event:
	Preprocesses the user input text.
	Creates a summarization pipeline.
	Generates a summary with a maximum length of 1 sentence and truncation.
	Displays the original text and the summary.
o	Creates an "About" section in the sidebar.
Running the Application
1.	Install dependencies: Run pip install streamlit nltk transformers in your terminal.
2.	Download NLTK resources: Use python -m nltk.downloader all to download necessary NLTK resources (may require additional steps depending on your environment).
3.	Run the app: Execute streamlit run streamlit_app.py in your terminal.
4.	Access the app: A web interface should open in your default browser at http://localhost:8501 by default.

