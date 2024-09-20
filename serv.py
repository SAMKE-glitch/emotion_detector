#!/usr/bin/env python3
import os
from flask import Flask, render_template, request
from EmotionDetection.clients.ibm_emotion_detector import IBEmotionDetector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask("Emotion detector")

# Fetch the API key and service URL from environment variables
api_key = os.getenv('IBM_API_KEY')
url = os.getenv('IBM_SERVICE_URL')

# Initialize IBM Emotion Detector
detector = IBEmotionDetector(api_key, url)
app = Flask("Emotion detector")

# Fetch the API key and service URL from environment variables
api_key = os.getenv('IBM_API_KEY')
url = os.getenv('IBM_SERVICE_URL')

# Initialize IBM Emotion Detector

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = detector.detect_emotion(text_to_analyze)
    display_string = "For the given statement, the system response is "
    emotions = list(response.keys())
    for i, emotion in enumerate(emotions):
        if i < len(emotions) - 1:
            display_string += f"'{emotion}': {response[emotion]}, "
        else:
            display_string += f"'{emotion}': {response[emotion]} and "
    display_string += f"The dominant emotion is {response['dominant_emotion']}."
    return display_string

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

