import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

from nltk import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import contractions

def clean_text(text):
    text = contractions.fix(text)
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    text = text.split()
    text = [w for w in text if not w in stop_words]
    text = " ".join(text)
    text = WordPunctTokenizer().tokenize(text)
    lemm = WordNetLemmatizer()
    text = [lemm.lemmatize(w) for w in text]
    text = " ".join(text)
    return text

model = pickle.load(open('../models/model.sav', 'rb'))
tf1 = pickle.load(open("../models/tfidf1.pkl", 'rb'))
tf1_new = TfidfVectorizer(vocabulary = tf1.vocabulary_)
classes = ["tix", "interests", "info", "fallback", "welcome", "slot filling"]
queries = [
    "one ticket",
    "1 ticket",
    "3 tickets please",
    "i would like a ticket",
    "can i get a ticket"
]
queries += [
    "i like the universe do you have something related",
    "i love science what exhibition can i go to",
    "i am interested in forests what do you suggest",
    "can you recommend an exhibition",
    "recommend exhibitions"
]
queries += [
    "what can you tell me about the antarctic base",
    "what exhibits do you have",
    "what's on",
    "who created the flooded forest",
    "will kids like the museum",
    "is the geological wall ok for kids"
]
queries += [
    "whats'up",
    "fuck off",
    "what do you want",
    "shut up",
    "lol",
    "ahskf"
]
queries += [
    "hey",
    "my name is davide",
    "what can you do?",
    "hello",
    "how are you?"
]
queries += [
    "1",
    "one",
    "five",
    "tomorrow",
    "next week",
    "i like architecture and water",
    "i like plants",
    "the flooded forest",
    "antarctic base"
]

def test(query):
    print(query)
    query = clean_text(query)
    query = tf1_new.fit_transform([query])
    pred = model.predict(query)[0]
    print(classes[pred])
    print()

for query in queries:
    test(query)