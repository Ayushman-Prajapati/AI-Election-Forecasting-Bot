import csv
import json
import os
from datetime import datetime
from collections import defaultdict

def save_to_csv(topic, score, label):
    with open("sentiment_trends.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), topic, score, label])

def forecast_trend(topic):
    try:
        with open("sentiment_trends.csv", mode="r") as file:
            reader = csv.reader(file)
            scores = [float(row[2]) for row in reader if row[1].lower() == topic.lower()]
            if len(scores) < 3:
                return "Insufficient data"
            avg = sum(scores[-3:]) / 3
            if avg > 0.7:
                return "Rising Support"
            elif avg < 0.3:
                return "Declining Support"
            else:
                return "Uncertain"
    except FileNotFoundError:
        return "No historical data"

# ✅ New function to generate chart data
def generate_chart_data(topic):
    timestamps = []
    scores = []

    try:
        with open("sentiment_trends.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1].lower() == topic.lower():
                    timestamps.append(row[0])
                    scores.append(float(row[2]))
    except FileNotFoundError:
        pass

    # Keep only last 7 entries
    timestamps = timestamps[-7:]
    scores = scores[-7:]

    os.makedirs("static", exist_ok=True)
    with open(f"static/sentiment_data_{topic.lower()}.json", "w") as f:
        json.dump({"timestamps": timestamps, "scores": scores}, f)
