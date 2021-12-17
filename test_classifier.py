import pandas as pd
from nltk import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import contractions
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

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

model = pickle.load(open('model.sav', 'rb'))
tf1 = pickle.load(open("tfidf1.pkl", 'rb'))
tf1_new = TfidfVectorizer(vocabulary = tf1.vocabulary_)
classes = ["tix", "interests", "info", "welcome", "fallback"]
query = "My favourite food is pasta"
query = clean_text(query)
query = tf1_new.fit_transform([query])
pred = model.predict(query)
print(classes[pred[0]])