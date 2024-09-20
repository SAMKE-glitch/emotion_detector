#!/usr/bin/env python3

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    # Construct the display string
    display_string = "For the given statement, the system response is "
    emotions = list(response.keys())
    for i, emotion in enumerate(emotions):
        if i < len(emotions) - 1:
            display_string += f"'{emotion}': {response[emotion]}, "
        else:
            display_string += f"'{emotion}': {response[emotion]} and "
    # Add the dominant emotion
    display_string += f"The dominant emotion is {response['dominant_emotion']}."
    return display_string

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

## after error handling
"""from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    
    # Check if dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    
    # Construct the display string
    display_string = "For the given statement, the system response is "
    emotions = list(response.keys())
    for i, emotion in enumerate(emotions):
        if i < len(emotions) - 1:
            display_string += f"'{emotion}': {response[emotion]}, "
        else:
            display_string += f"'{emotion}': {response[emotion]} and "
    
    # Add the dominant emotion
    display_string += f"The dominant emotion is {response['dominant_emotion']}."
    
    return display_string

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
"""
