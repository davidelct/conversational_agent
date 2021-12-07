import spacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
doc = nlp("One ticket for the Caixa museum, space, please.")
interests = ['universe', 'space', 'cosmos', 'brain', 'interactive', 'big bang', 'evolution', 'science', 'life', 'physics', 'earth', 'sun', 'moon', 'mars', 'light', 'gravity', 'matter', 'planets', 'stars', 'nature', 'technology', 'floodings', 'forest', 'jungle', 'amazon', 'plants', 'water', 'ecosystem', 'biodiversity', 'brazil',
             'south america', 'animals', 'climate', 'climate change', 'rivers', 'temperature', 'national geographic', 'photos', 'ecology', 'organisms', 'environment', 'photographer', 'polar', 'exploration', 'erosion', 'vulcanos', 'rock', 'rocks', 'landscape', 'earthquakes', 'green', 'sustainability', 'education', 'efficiency', 'building', 'architecture']

exhibit_names = ['universe room', 'flooded forest',
                 'antarctic base', 'geological wall', 'sustainable building']

i = 0
for token in doc:
  if str(token) in interests:
    doc.ents += (Span(doc, i, i+1, "INTEREST"),)
  if str(token) in exhibit_names:
    doc.ents += (Span(doc, i, i+1, "EXHIBITS"),)
  i+=1

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)