from flask import Flask, request, jsonify
import joblib

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
def download_nltk_resources():
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet')

download_nltk_resources()

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Load the model and vectorizer
model = joblib.load('news_bias_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

app = Flask(__name__)

# Preprocessing function (you should implement this)
def preprocess_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove non-alphabetical characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords and lemmatize
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    
    # Join tokens back into a single string
    return ' '.join(tokens)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict_bias():
    data = request.get_json()  # Get JSON data from request
    news_content = data.get('content', '')  # Get 'content' field
    cleaned_content = preprocess_text(news_content)  # Preprocess the text
    transformed_content = tfidf.transform([cleaned_content])  # Transform using TF-IDF
    prediction = model.predict(transformed_content)[0]  # Predict bias

    # Map bias values to labels
    bias_map = {0: 'Left', 1: 'Center', 2: 'Right'}
    bias_label = bias_map[prediction]
    return jsonify({'bias': bias_label})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
