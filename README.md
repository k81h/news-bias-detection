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

### 1. Clone the Repository

```bash
git clone https://github.com/k81h/news-bias-detection
cd news-bias-detection
```

### 2. Set Up a Virtual Environment

Setting up a virtual environment ensures that all dependencies are installed in an isolated environment, avoiding conflicts with other projects.

- **Create a virtual environment**:
  
  On Windows:
  ```bash
  python -m venv venv
  ```

  On macOS/Linux:
  ```bash
  python3 -m venv venv
  ```

- **Activate the virtual environment**:

  On Windows:
  ```bash
  venv\Scripts\activate
  ```

  On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

After installing the dependencies, run the Flask app:

```bash
python app.py
```

### 5. Test the API

You can use the following PowerShell command to test the API:

```powershell
(Invoke-WebRequest -Uri "http://localhost:5000/predict" -Method Post -Headers @{"Content-Type"="application/json"} -Body (ConvertTo-Json @{content="Sample text."})).Content | ConvertFrom-Json | Select-Object -ExpandProperty bias
```

This command sends a POST request to the API with the content "Sample text." and outputs the predicted bias.

To use this command:
1. Open PowerShell
2. Copy and paste the command
3. Replace "Sample text." with your desired news article text
4. Press Enter to execute

The command will output the predicted bias: "Left", "Center", or "Right".
