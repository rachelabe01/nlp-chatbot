import csv

# Specify the path to your CSV file containing questions and answers
csv_file_path = 'C:/Users/rachel/OneDrive/Desktop/nlp/output.csv'

# Define your custom Hindi lemmatization dictionary
word_to_lemma = {"करना": "कर",
    "महत्वपूर्ण": "महत्व",
    "सीखने": "सीखना",
    "सोचने ": "सोचना",
    "देती ": "देना",
    "पढ़ाई  ": "पढ़ा",
    "शिक्षकों" : "शिक्षक",
    "छात्रों" : "छात्र",
    "मिलकरना" : "मिल",
    "तैयारी" :  "तैयार",
    "करें" : "कर",
    "सीखने" : "सीख",
    "उच्चतर" : "उच्च",
    "स्नातक" : "स्नान",
    "स्नातकोत्तर" : "स्नातक",
    "कार्यक्रमों" : "कार्यक्रम",
    "मिलकरने" : "मिल",
    "विचारशीलता" : "विचारशील",
    "भागीदारी" : "भागीदार",
    "योग्यता" : "योग्य",
    "स्नातक" : "स्नान",
    "चुनें" : "चुन",
    "सार्थकता": "सार्थक",
    "स्वतंत्रता": "स्वतंत्र",
    "लक्ष्य" : "लक्ष",
    "प्राथमिकता" : "प्राथमिक",
    "प्रौद्योगिकी" : "प्रौद्योगिक",
    "तकनीकी" : "तकनीक",
    # Your lemmatization mappings
}

# Define your custom stopwords
custom_stopwords = [
    "क्या", "का","है", "की", "के", "को", "है", "हैं", "में", "से", "पर", "इस", "इसके",
    "उस", "उसके", "कि", "जो", "था", "थे", "कर", "करता", "करते", "किया", "किए",
    # Add more stopwords as needed
]

# Initialize empty dictionaries to store the lemmatized questions and answers
question_to_lemma = {}
answer_to_lemma = {}

# Read the CSV file and populate the dictionaries
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if it exists

    for row in reader:
        if len(row) >= 2:
            question, answer = row[0], row[1]

            # Lemmatize the question and answer using the custom dictionary
            lemmatized_question = ' '.join([word_to_lemma.get(word, word) for word in question.split() if word not in custom_stopwords])
            lemmatized_answer = ' '.join([word_to_lemma.get(word, word) for word in answer.split() if word not in custom_stopwords])

            # Store the lemmatized question and answer in the dictionaries
            question_to_lemma[question] = lemmatized_question
            answer_to_lemma[answer] = lemmatized_answer

# Print the word-to-lemma mapping for questions
for question, lemma in question_to_lemma.items():
    print(f'Question: {question}, Lemma: {lemma}')

# Print the word-to-lemma mapping for answers
for answer, lemma in answer_to_lemma.items():
    print(f'Answer: {answer}, Lemma: {lemma}')