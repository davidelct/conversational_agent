import spacy
from utils import clean_text

def parse(query):
    nlp = spacy.load("models/spacy_model/")
    query = clean_text(query)
    doc = nlp(query)
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    return doc.ents
