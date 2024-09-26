# News Bias Detection API

This project provides an API that classifies news articles as "Left", "Center", or "Right" based on their content. The model uses machine learning (Logistic Regression/Naive Bayes) and TF-IDF vectorization for text classification.

## Features

- Accepts either raw text content or a URL to a news article.
- Predicts the political bias of the article.
  
## Project Structure

```
news-bias-detection/
├── app.py                   # Your main Flask app
├── news_bias_model.pkl       # Pre-trained bias prediction model
├── tfidf_vectorizer.pkl      # TF-IDF vectorizer
├── requirements.txt          # List of Python dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files/folders to ignore by Git
```

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/news-bias-detection.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Test the API by sending a POST request to `http://127.0.0.1:5000/predict` with either a URL or content.

## Example Request

```json
{
  "content": "Sample text"
}
```

## Example Response

```json
{
  "bias": "Center"
}
```
