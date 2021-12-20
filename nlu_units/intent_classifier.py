from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from utils import clean_text

class IntentClassifier:

    def __init__(self, classifier_path, vectorizer_path):
        self.classifier = pickle.load(open(classifier_path, "rb"))
        vectorizer = pickle.load(open(vectorizer_path, "rb"))
        self.vectorizer = TfidfVectorizer(vocabulary = vectorizer.vocabulary_)

    def classify_intent(self, sentence):
        intents = ["tickets", "interests", "info", "fallback", "welcome", 
            "slot filling"]
        sentence = clean_text(sentence)
        sentence = self.vectorizer.fit_transform([sentence])
        prediction = self.classifier.predict(sentence)[0]
        return intents[prediction]