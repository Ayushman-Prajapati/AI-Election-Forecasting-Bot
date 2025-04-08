from flask import Flask, render_template, request
from news_fetcher import fetch_news
from sentiment_analyzer import analyze_sentiment
from trend_tracker import save_to_csv, forecast_trend, generate_chart_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    topic = request.form['topic']
    headlines = fetch_news(topic)

    sentiments = []
    for headline in headlines:
        sentiment = analyze_sentiment(headline)
        sentiments.append(sentiment)
        save_to_csv(topic, sentiment['score'], sentiment['label'])

    generate_chart_data(topic)

    pos_count = sum(1 for s in sentiments if s['label'] == 'POSITIVE')
    neg_count = sum(1 for s in sentiments if s['label'] == 'NEGATIVE')
    prediction = "Likely Support" if pos_count >= neg_count else "Likely Opposition"

    results = zip(headlines, sentiments)
    forecast = forecast_trend(topic)

    return render_template('result.html', topic=topic, prediction=prediction, forecast=forecast, results=results)

if __name__ == '__main__':
    app.run(debug=True)
