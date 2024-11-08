from flask import Flask, render_template, request, jsonify
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize the Flask app
app = Flask(__name__)

# Download necessary NLTK resources if not already downloaded
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

# Initialize the lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Load the model and vectorizer
model = joblib.load('news_bias_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

# Preprocessing function (text cleaning)
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

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the news content from the form
        news_content = request.form['news_content']
        
        if news_content:
            # Preprocess the input text
            cleaned_content = preprocess_text(news_content)
            
            # Transform the cleaned content using the TF-IDF vectorizer
            transformed_content = tfidf.transform([cleaned_content])
            
            # Predict bias
            prediction = model.predict(transformed_content)[0]
            
            # Map bias values to labels
            bias_map = {0: 'Left', 1: 'Center', 2: 'Right'}
            bias_label = bias_map[prediction]
            
            return render_template('index.html', prediction=bias_label, news_content=news_content)
        else:
            return render_template('index.html', error="Please enter some content to predict the bias.")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
