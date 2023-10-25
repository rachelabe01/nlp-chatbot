import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the CSV file with UTF-8 encoding
df = pd.read_csv("output.csv", encoding="utf-8")

# Create a dataset dictionary
qa_dataset = dict(zip(df["Question"].str.lower(), df["Answer"]))

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(qa_dataset.keys())

# Define the chatbot function
def hindi_chatbot(user_input, chat_history):
    user_input = user_input.lower()
    chat_history.append(f"आप: {user_input}")
    
    if user_input in qa_dataset:
        chat_history.append(f"चैटबॉट: {qa_dataset[user_input]}")
    else:
        # Transform the user input into a TF-IDF vector
        user_tfidf = tfidf_vectorizer.transform([user_input])

        # Calculate cosine similarities between the user input and dataset questions
        similarities = cosine_similarity(user_tfidf, tfidf_matrix)

        # Find the most similar question
        max_similarity_index = similarities.argmax()
        most_similar_question = list(qa_dataset.keys())[max_similarity_index]
        answer = qa_dataset.get(most_similar_question, "मुझे खेद है, मैं उस सवाल का जवाब नहीं दे सकता।")
        chat_history.append(f"चैटबॉट: {answer}")

    return chat_history

# Create a Streamlit app
st.title("Hindi Chatbot")

# Initialize or load the chat history list
chat_history = st.session_state.get("chat_history", [])

# Create an input text box for user input
user_input = st.text_input("आपका सवाल यहाँ लिखें:")

if st.button("प्रेषित करें") and user_input:
    chat_history = hindi_chatbot(user_input, chat_history)

# Save the chat history to the session state for persistence
st.session_state.chat_history = chat_history

# Display the chat history continuously
st.text("\n".join(chat_history))
