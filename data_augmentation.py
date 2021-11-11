import pandas as pd
import nlpaug.augmenter.word as naw
import torch

path_to_ticket_samples = "Tickets.txt"
with open(path_to_ticket_samples) as f:
    ticket_sentences = f.readlines()

aug = naw.RandomWordAug()
aug_ticket_sentences = aug.augment(ticket_sentences)
print(aug_ticket_sentences)



#https://nlpaug.readthedocs.io/en/latest/augmenter/word/random.html
