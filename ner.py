import spacy
from utils import clean_text

class EntityExtractor:

    def __init__(self, spacy_model_path):
        self.model = spacy.load(spacy_model_path)

    def parse(self, query):
        query = clean_text(query)
        doc = self.model(query)
        return doc.ents