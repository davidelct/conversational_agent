import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from test_classifier import clean_text

def get_intent(query):
    model = pickle.load(open('model.sav', 'rb'))
    tf1 = pickle.load(open("tfidf1.pkl", 'rb'))
    tf1_new = TfidfVectorizer(vocabulary = tf1.vocabulary_)
    classes = ["tix", "interests", "info", "fallback", "welcome"]
    query = clean_text(query)
    query = tf1_new.fit_transform([query])
    pred = model.predict(query)
    return classes[pred[0]]

