import json
import requests

def emotion_detector(text_to_analyze):
    '''
    Function that analyzes text and returns a dictionary containing the required set of emotions with their scores,
    along with the dominant emotion.
    '''
    if not text_to_analyze:
        # Handle blank entries
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=Input, headers=Headers)
    
    if response.status_code == 400:
        # Handle HTTP 400 error
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    try:
        formated_response = json.loads(response.text)
        # Extracting the emotion scores
        emotion_scores = formated_response['emotionPredictions'][0]['emotion']
        # Required set of emotions
        required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        # Finding dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        # Construct the dictionary containing the required set of emotions along with their scores
        result = {emotion: emotion_scores.get(emotion, 0) for emotion in required_emotions}
        # Add the dominant emotion to the result dictionary
        result['dominant_emotion'] = dominant_emotion
        return result
    except Exception as e:
        # Handle any other errors
        print(f"Error: {e}")
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
