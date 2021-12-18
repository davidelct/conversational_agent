from nltk.corpus import switchboard
import nltk
from random import sample
import csv
import pandas
import nlpaug.augmenter.word as naw
#nltk.download("switchboard")
stopwords = ["uh", "Uh", "um", "Um", "Uh-huh", "uh-huh", "Huh", "huh", "Yeah", "yeah", ",", "--", ".", "-"] 
welcome = ["hi", "hello", "hey", "helloo", "hellooo", "heya","Can I ask you something?", "hello hi","Can you help me?","Can you help me with something?", "I need some help", "howdy", "hi there", "hey there", "hello there", "lovely day isn't it", "I greet you", "hello again", "long time no see", "just going to say hi", "g morining", "gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "good night", "greetings", "greeting","its nice to meet you", "nice to meet you", "nice meeting you", "nice to see you", "its nice seeing you","its nice to see you", "its good to see you", "good to see you", "a good day", "a good afternoon", "a good morning", "a good night", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", "g’day", "howdy"]
sentences = switchboard.turns()
new_sentences = []
for sent in sentences:
    new_sent = ""
    for word in sent:
        if not (word in stopwords):
            if not(word == "." and len(new_sent)==0):
                new_sent += word + " "
    if len(new_sent)>20 and len(new_sent)<125:
        new_sentences.append(new_sent)
sample_sents = sample(new_sentences, 600)
extra_sents = ["i want to go flying", "i want to go diving", "i want to go on an adventure", "i want to buy a book", "i want to buy some clothes", "i want to buy fruit", "i want to get drunk", "i'd like some fries"]
with open("data/augmented/fallback.txt", "w") as f:
    for sentence in sample_sents:
        f.write(sentence)
        f.write("\n")
    for sentence in extra_sents:
        f.write(sentence)
        f.write("\n")

with open("data/augmented/fallback.csv", "w") as f:
    f.write("phrase,class")
    f.write("\n")
    for sentence in sample_sents:
        f.write(sentence + ",3")
        f.write("\n")
    for sentence in extra_sents:
        f.write(sentence + ",3")
        f.write("\n")

with open("names.txt", "r") as f:
    names = f.readlines()

sample_names = sample(names, 30)
names = []
for name in sample_names:
    names.append(name[:len(name)-1])

aug2 = naw.BackTranslationAug()
aug2_welcome = aug2.augment(welcome)

def combine_lists(original, new):
    result = original
    for sentence in new:
        if sentence not in result:
            result.append(sentence)
    return result

new_welcome = combine_lists(welcome, aug2_welcome)
for name in names:
    new_welcome.append("My name is " + name)
    new_welcome.append("I am " + name)
    new_welcome.append("You can call me " + name)
    new_welcome.append("I am called " + name)

with open("data/augmented/welcome.txt", "w") as f:
    for sentence in new_welcome:
        f.write(sentence)
        f.write("\n")


with open("data/augmented/welcome.csv", "w") as f:
    f.write("phrase,class")
    f.write("\n")
    for sentence in new_welcome:
        f.write(sentence + ",4")
        f.write("\n")