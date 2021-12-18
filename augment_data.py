from datetime import date, timedelta
from dateutil.relativedelta import *
from collections import OrderedDict
from random import sample


def augment(path_to_data, output_path, csv_output_path, label, sample_size=0, short=False):
    numbers = ['two', 'three', 'four', 'five', 'six']

    interests = ['universe', 'space', 'cosmos', 'brain', 'big bang', 'evolution', 'science', 'life', 'physics', 'earth', 'sun', 'moon', 'mars', 'light', 'gravity', 'matter', 'planets', 'stars', 'nature', 'technology', 'floodings', 'forest', 'jungle', 'amazon', 'plants', 'water', 'ecosystem', 'biodiversity', 'brazil',
                 'south america', 'animals', 'climate', 'climate change', 'rivers', 'temperature', 'national geographic', 'photos', 'ecology', 'organisms', 'environment', 'photographer', 'exploration', 'erosion', 'vulcanos', 'rock', 'rocks', 'landscape', 'earthquakes', 'sustainability', 'education', 'efficiency', 'building', 'architecture']

    exhibit_names = ['universe room', 'flooded forest',
                     'antarctic base', 'geological wall', 'sustainable building']

    today = date.today()
    end_date = today + relativedelta(months=+12)
    delta = end_date - today
    dates = [(today + timedelta(days=i)) for i in range(delta.days + 1)]
    db = [day.strftime("%d %b") for day in dates]
    bd = [day.strftime("%b %d") for day in dates]
    db = ["for " + day for day in db]
    bd = ["for " + day for day in bd]
    dates1 = db
    dates1 = dates1 + bd

    days1 = ["for today", "for tomorrow"]
    days1 = days1 + ["for Monday", "on Tuesday", "on Wednesday", "on Thursday", "on Friday", "on Saturday", "on Sunday"]
    days1 = days1 + ["for this Monday", "for this Tuesday", "for this Wednesday", "for this Thursday", "for this Friday", "for this Saturday", "for this Sunday"]
    days1 = days1 + ["for next Monday", "for next Tuesday", "for next Wednesday", "for next Thursday", "for next Friday", "for next Saturday", "for next Sunday"]
    days1 = days1 + ["for this week", "for next week"]
    days1 = days1 + ["for this weekend", "for next weekend"]
    days1 = days1 + ["for this month", "for next month"]

    db = [day.strftime("%d %b") for day in dates]
    bd = [day.strftime("%b %d") for day in dates]
    db = ["on " + day for day in db]
    bd = ["on " + day for day in bd]
    dates2 = db
    dates2 = dates2 + bd

    days2 = ["today", "tomorrow"]
    days2 = days2 + ["on Monday", "on Tuesday", "on Wednesday", "on Thursday", "on Friday", "on Saturday", "on Sunday"]
    days2 = days2 + ["this Monday", "this Tuesday", "this Wednesday", "this Thursday", "this Friday", "this Saturday", "this Sunday"]
    days2 = days2 + ["next Monday", "next Tuesday", "next Wednesday", "next Thursday", "next Friday", "next Saturday", "next Sunday"]
    days2 = days2 + ["this week", "next week"]
    days2 = days2 + ["this weekend", "next weekend"]
    days2 = days2 + ["this month", "next month"]

    f = open(path_to_data, 'r')
    phrases = f.readlines()

    num_augmented_phrases = []

    for phrase in phrases:
        tokenized = phrase.lower().split()
        if '[number]' in tokenized:
            for i, token in enumerate(tokenized):
                if 'number' in token:
                    break
            for num in numbers:
                tokenized[i] = num
                num_augmented_phrases.append(' '.join(tokenized))
        else:
            num_augmented_phrases.append(' '.join(tokenized))

    int_augmented_phrases = []
    for phrase in num_augmented_phrases:
        tokenized = phrase.split()
        if '[exhibition_topic]' in tokenized:
            for i, token in enumerate(tokenized):
                if 'exhibition_topic' in token:
                    break
            if short:
                rinterest = sample(interests, sample_size)
            else:
                rinterest = interests
            for interest in rinterest:
                tokenized[i] = interest
                int_augmented_phrases.append(' '.join(tokenized))
        else:
            int_augmented_phrases.append(' '.join(tokenized))

    exhibit_augmented_phrases = []
    for phrase in int_augmented_phrases:
        tokenized = phrase.split()
        if '[exhibition_name]' in tokenized:
            for i, token in enumerate(tokenized):
                if 'exhibition_name' in token:
                    break
            for exhibit in exhibit_names:
                tokenized[i] = exhibit
                exhibit_augmented_phrases.append(' '.join(tokenized))
        else:
            exhibit_augmented_phrases.append(' '.join(tokenized))

    dates_augmented_phrases = []
    for phrase in exhibit_augmented_phrases:
        tokenized = phrase.split()
        if '[date1]' in tokenized:
            for i, token in enumerate(tokenized):
                if 'date1' in token:
                    break
            if short:
                rdates = sample(dates1, sample_size)
                rdays = sample(days1, sample_size)
            else:
                rdates = dates1
                rdays = days1
            for d in rdates:
                tokenized[i] = d
                dates_augmented_phrases.append(' '.join(tokenized))
            for d in rdays:
                tokenized[i] = d
                dates_augmented_phrases.append(' '.join(tokenized))
        elif '[date2]' in tokenized:
            for i, token in enumerate(tokenized):
                if 'date2' in token:
                    break
            if short:
                rdates = sample(dates2, sample_size)
                rdays = sample(days2, sample_size)
            else:
                rdates = dates2
                rdays = days2
            for d in rdates:
                tokenized[i] = d
                dates_augmented_phrases.append(' '.join(tokenized))
            for d in rdays:
                tokenized[i] = d
                dates_augmented_phrases.append(' '.join(tokenized))
        else:
            dates_augmented_phrases.append(' '.join(tokenized))

    dates_augmented_phrases = list(OrderedDict.fromkeys(dates_augmented_phrases))

    f = open(output_path, 'w')
    for phrase in dates_augmented_phrases:
        f.write(phrase)
        f.write('\n')

    with open(csv_output_path, "w") as f:
        f.write("phrase,class")
        f.write("\n")
        for sentence in dates_augmented_phrases:
            f.write(sentence +","+ str(label))
            f.write("\n")


path_to_tix = 'data/tix.txt'
path_to_info = 'data/info.txt'
path_to_interests = 'data/interests.txt'

augment(path_to_tix, 'data/augmented/tix.txt','data/augmented/tix.csv', 0, sample_size = 4, short=True)
augment(path_to_info, 'data/augmented/info.txt', 'data/augmented/info.csv',2, sample_size= 29, short=True)
augment(path_to_interests, 'data/augmented/interests.txt', 'data/augmented/interests.csv', 1)
