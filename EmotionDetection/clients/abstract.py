# EmotionDetection/clients/abstract.py
from abc import ABC, abstractmethod

class AbstractEmotionDetector(ABC):
    @abstractmethod
    def detect_emotion(self, text):
        """Analyze emotions from the text and return a result."""
        pass
