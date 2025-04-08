import requests

def fetch_news(topic):
    API_KEY = "eaa3fcd5e29f408bb4434c9505ba01d4"  # Replace with your NewsAPI key
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&language=en&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    headlines = [article["title"] for article in data["articles"][:5]]
    return headlines
