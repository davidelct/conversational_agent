import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from utils import clean_text

model = pickle.load(open('model.sav', 'rb'))
tf1 = pickle.load(open("tfidf1.pkl", 'rb'))
tf1_new = TfidfVectorizer(vocabulary = tf1.vocabulary_)
classes = ["tix", "interests", "info", "fallback", "welcome"]
query = "i broke my foot"
query = clean_text(query)
query = tf1_new.fit_transform([query])
pred = model.predict(query)
print(pred)
print(classes[pred[0]])