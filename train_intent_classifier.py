import pandas as pd
from nltk import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import contractions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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


tix = pd.read_csv("data/augmented/tix.csv")
interests = pd.read_csv("data/augmented/interests.csv")
info = pd.read_csv("data/augmented/info.csv")
welcome = pd.read_csv("data/augmented/welcome.csv")
fallback = pd.read_csv("data/augmented/fallback.csv")
df = pd.concat([tix, interests, info, fallback, welcome])
df = df.sample(frac=1).reset_index(drop=True)
df.phrase = df.phrase.astype(str)
df['phrase'] = df['phrase'].apply(clean_text)
df.to_csv("df.csv",index=False)

vectorizer = TfidfVectorizer()
X = df['phrase'].tolist()
X = vectorizer.fit_transform(X)
pickle.dump(vectorizer, open("tfidf1.pkl", "wb"))
y = df['class'].tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train)

y_hat = model.predict(X_test)
print(accuracy_score(y_test,y_hat))
pickle.dump(model, open('model.sav', 'wb'))