from numpy import not_equal
import spacy
from spacy.tokens import Span
from nltk.corpus import wordnet
import nltk
import pandas
import gensim
from collections import OrderedDict
import json

def get_entities(sentence, interest_dict, exhibit_names):
  nlp = spacy.load("en_core_web_sm")
  doc = nlp(sentence)
  i = 0
  for token in doc:
    if str(token) not in [ent.text for ent in doc.ents]:
      if str(token) in exhibit_names:
        doc.ents += (Span(doc, i, i+1, "EXHIBITS"),)
      else:
        for key in interest_dict:
          if str(token) == key:
            doc.ents += (Span(doc, i, i+1, "INTEREST"),)
            break
          else:
            for value in interest_dict[key]:
              if str(token) == value:
                doc.ents += (Span(doc, i, i+1, "INTEREST"),)   
                break
            break
    i+=1
  return doc.ents
  
def get_interests():
  with open("new_interest.txt") as f:
    text = f.readlines()
    dict = json.loads(text[0])
    
  return dict

'''
interests = ['universe', 'space', 'cosmos', 'brain', 'interactive', 'big bang', 'evolution', 'science', 'life', 'physics', 'earth', 'sun', 'moon', 'mars', 'light', 'gravity', 'matter', 'planets', 'stars', 'nature', 'technology', 'floodings', 'forest', 'jungle', 'amazon', 'plants', 'water', 'ecosystem', 'biodiversity', 'brazil',
             'south america', 'animals', 'climate', 'climate change', 'rivers', 'temperature', 'national geographic', 'photos', 'ecology', 'organisms', 'environment', 'photographer', 'polar', 'exploration', 'erosion', 'vulcanos', 'rock', 'rocks', 'landscape', 'earthquakes', 'green', 'sustainability', 'education', 'efficiency', 'building', 'architecture']
interest_list = [interest for interest in interests]

path_to_word2vec_sample = nltk.data.find('models/word2vec_sample/pruned.word2vec.txt')
word2vec_gensim = gensim.models.KeyedVectors.load_word2vec_format(path_to_word2vec_sample)
new_interests = {}
for interest in interests:
  if interest in word2vec_gensim:
    similar_words = word2vec_gensim.most_similar(interest, topn = 10)
    for word in similar_words:
      if interest in new_interests:
        new_interests[interest].append(word[0])
      else:
        new_interests[interest] = [word[0]]

f = open('new_interest.txt', 'w')
f.write(json.dumps(new_interests))
'''




# Find named entities, phrases and concepts
#for entity in doc.ents:
 #   print(entity.text, entity.label_)

