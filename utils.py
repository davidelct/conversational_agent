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