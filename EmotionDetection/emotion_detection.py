
from dotenv import load_dotenv
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Load environment variables from .env file
load_dotenv()

# Get API key and URL from the environment variables
api_key = os.getenv('IBM_API_KEY')
url = os.getenv('IBM_SERVICE_URL')
def emotion_detector(text_to_analyze):
    '''
    Function that analyzes text and returns a dictionary containing the required set of emotions with their scores,
    along with the dominant emotion.
    '''

    if not text_to_analyze:
        # Handle blank entries
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    # Set up the authenticator
    authenticator = IAMAuthenticator(api_key)
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )

    # Set the service URL
    nlu.set_service_url(url)

    # Analyze the emotions in the text
    try:
        response = nlu.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        ).get_result()

        # Extracting emotion scores
        emotion_scores = response['emotion']['document']['emotion']
        required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        result = {emotion: emotion_scores.get(emotion, 0) for emotion in required_emotions}
        result['dominant_emotion'] = dominant_emotion

        return result

    except Exception as e:
        print(f"Error: {e}")
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

