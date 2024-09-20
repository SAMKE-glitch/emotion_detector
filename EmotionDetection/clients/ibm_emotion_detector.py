# EmotionDetection/clients/ibm_emotion_detector.py
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from .abstract import AbstractEmotionDetector

class IBEmotionDetector(AbstractEmotionDetector):
    def __init__(self, api_key, url):
        self.authenticator = IAMAuthenticator(api_key)
        self.nlu = NaturalLanguageUnderstandingV1(
            version='2021-08-01',
            authenticator=self.authenticator
        )
        self.nlu.set_service_url(url)

    def detect_emotion(self, text_to_analyze):
        if not text_to_analyze:
            return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

        try:
            response = self.nlu.analyze(
                text=text_to_analyze,
                features=Features(emotion=EmotionOptions())
            ).get_result()

            emotion_scores = response['emotion']['document']['emotion']
            required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            result = {emotion: emotion_scores.get(emotion, 0) for emotion in required_emotions}
            result['dominant_emotion'] = dominant_emotion

            return result

        except Exception as e:
            print(f"Error: {e}")
            return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

