from transformers import pipeline

# Load model once
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_model(text)[0]
    return {"label": result["label"], "score": result["score"]}
