from abc import ABC, abstractmethod
import pyttsx3
from transformers import pipeline
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

class AIModel(ABC):
    @abstractmethod
    def run(self, input_text):
        pass

class TTSModel(AIModel):
    def __init__(self):
        self.engine = pyttsx3.init()

    @timing_decorator
    def run(self, input_text):
        self.engine.say(input_text)
        self.engine.runAndWait()

class SummarizerModel(AIModel):
    def __init__(self):
        self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    @timing_decorator
    def run(self, input_text):
        summary = self.summarizer(input_text, max_length=60, min_length=20, do_sample=False)
        return summary[0]['summary_text']
