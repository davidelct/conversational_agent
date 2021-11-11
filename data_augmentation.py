import pandas as pd
import nlpaug.augmenter.word as naw
from nltk.corpus import stopwords
#import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')
stops = [stopwords.words('english')]

path_to_ticket_samples = "Tickets.txt"
with open(path_to_ticket_samples) as f:
    ticket_sentences = f.readlines()

aug = naw.RandomWordAug(action='swap', stopwords=stops)
aug_ticket_sentences = aug.augment(ticket_sentences)
#print(aug_ticket_sentences)

#aug2 = naw.BackTranslationAug()
#aug2_ticket_sentences = aug2.augment(ticket_sentences)
#print(aug2_ticket_sentences)

aug3 = naw.SynonymAug(stopwords=stops)
aug3_ticket_sentences = aug3.augment(ticket_sentences)
print(aug3_ticket_sentences)

def remove_stopwords(list_of_sentences):
    result = []
    for sentence in list_of_sentences:
        tokens = sentence.split()
        new_sentence = ""
        for token in tokens:
            if token not in stops:
                new_sentence+=token
        result.append(new_sentence)
    return result

def combine_lists(original, new):
    result = original
    for sentence in new:
        if sentence not in result:
            result.append(original)
    return result

#https://nlpaug.readthedocs.io/en/latest/augmenter/word/random.html
