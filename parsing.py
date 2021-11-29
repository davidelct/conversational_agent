import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I love space, which exhibition should I go to?")
# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

for token in doc:
  print(str(token) + " : " + token.pos_ + " (" + token.lemma_ + ")")

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)