"""
# EmotionDetection/emotion_detection.py
#from clients.ibm_emotion_detector import IBEmotionDetector
from EmotionDetection.clients.ibm_emotion_detector import IBEmotionDetector


# Initialize the detector with your API credentials
api_key = 'QAmaBGAJ7ook3UueHHQSy0UEqgoougTcR_c8U88D6KbM'
url = 'https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/75cc7845-fe8c-4877-81e3-f5bcd467b69e'

detector = IBEmotionDetector(api_key, url)

# Example usage
text = "I am feeling great!"
result = detector.detect_emotion(text)
print(result)
"""
import os
from dotenv import load_dotenv
from EmotionDetection.clients.ibm_emotion_detector import IBEmotionDetector

# Load environment variables from .env file
load_dotenv()

# Initialize the detector with your API credentials from the .env file
api_key = os.getenv('IBM_API_KEY')
url = os.getenv('IBM_SERVICE_URL')

detector = IBEmotionDetector(api_key, url)

# Example usage
text = "I am feeling great!"
result = detector.detect_emotion(text)
print(result)


