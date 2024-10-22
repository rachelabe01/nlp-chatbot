# Hindi Chatbot

A simple yet effective Hindi language chatbot built with Streamlit, featuring custom text preprocessing and TF-IDF-based response matching.

## Features

- Hindi language support
- Custom lemmatization for Hindi words
- TF-IDF vectorization for intelligent response matching
- User-friendly web interface built with Streamlit
- Persistent chat history during sessions
- Custom stopword removal

## Prerequisites

```
python >= 3.6
streamlit
pandas
scikit-learn
```

## Project Structure

```
├── chatbot.py          # Main chatbot application
├── preprocessing.py    # Text preprocessing utilities
└── output.csv         # Question-Answer dataset (not included)
```

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd hindi-chatbot
```

2. Install required packages:
```bash
pip install streamlit pandas scikit-learn
```

## Usage

1. Prepare your question-answer dataset in a CSV file named `output.csv` with columns "Question" and "Answer".

2. Run the preprocessing script to prepare the text data:
```bash
python preprocessing.py
```

3. Launch the chatbot web interface:
```bash
streamlit run chatbot.py
```

## How It Works

### Text Preprocessing (`preprocessing.py`)
- Implements custom Hindi lemmatization using a predefined dictionary
- Removes common Hindi stopwords
- Processes both questions and answers from the dataset
- Creates word-to-lemma mappings for improved matching

### Chatbot Implementation (`chatbot.py`)
- Uses TF-IDF vectorization to convert text into numerical features
- Implements cosine similarity for finding the best matching responses
- Maintains chat history during the session
- Provides fallback responses when no good match is found

## Customization

### Adding New Words to Lemmatization
Add new word-to-lemma mappings in `preprocessing.py`:
```python
word_to_lemma = {
    "नया_शब्द": "मूल_रूप",
    # Add more mappings
}
```

### Adding Stopwords
Add new stopwords in `preprocessing.py`:
```python
custom_stopwords = [
    "नया_स्टॉपवर्ड",
    # Add more stopwords
}
```

## Contributing

Feel free to submit issues and enhancement requests.
