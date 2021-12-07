from datetime import date, timedelta
from dateutil.relativedelta import *


def augment(path_to_data, output_path):
    numbers = ['two', 'three', 'four', 'five', 'six']

    interests = ['universe', 'space', 'cosmos', 'brain', 'interactive', 'big bang', 'evolution', 'science', 'life', 'physics', 'earth', 'sun', 'moon', 'mars', 'light', 'gravity', 'matter', 'planets', 'stars', 'nature', 'technology', 'floodings', 'forest', 'jungle', 'amazon', 'plants', 'water', 'ecosystem', 'biodiversity', 'brazil',
                 'south america', 'animals', 'climate', 'climate change', 'rivers', 'temperature', 'national geographic', 'photos', 'ecology', 'organisms', 'environment', 'photographer', 'polar', 'exploration', 'erosion', 'vulcanos', 'rock', 'rocks', 'landscape', 'earthquakes', 'green', 'sustainability', 'education', 'efficiency', 'building', 'architecture']

    exhibit_names = ['universe room', 'flooded forest',
                     'antarctic base', 'geological wall', 'sustainable building']

    today = date.today()
    end_date = today + relativedelta(months=+2)
    delta = end_date - today
    dates = [(today + timedelta(days=i)) for i in range(delta.days + 1)]

    f = open(path_to_data, 'r')
    phrases = f.readlines()

    num_augmented_phrases = []

    for phrase in phrases:
        tokenized = phrase.split()
        if '[NUMBER]' in tokenized:
            for i, token in enumerate(tokenized):
                if 'NUMBER' in token:
                    break
            for num in numbers:
                tokenized[i] = num
                num_augmented_phrases.append(' '.join(tokenized))
        else:
            num_augmented_phrases.append(' '.join(tokenized))

    int_augmented_phrases = []
    for phrase in num_augmented_phrases:
        tokenized = phrase.split()
        if '[EXHIBITION_TOPIC]' in tokenized:
            for i, token in enumerate(tokenized):
                if 'EXHIBITION_TOPIC' in token:
                    break
            for interest in interests:
                tokenized[i] = interest
                int_augmented_phrases.append(' '.join(tokenized))
        else:
            int_augmented_phrases.append(' '.join(tokenized))

    exhibit_augmented_phrases = []
    for phrase in int_augmented_phrases:
        tokenized = phrase.split()
        if '[EXHIBITION_NAME]' in tokenized:
            for i, token in enumerate(tokenized):
                if 'EXHIBITION_NAME' in token:
                    break
            for exhibit in exhibit_names:
                tokenized[i] = exhibit
                exhibit_augmented_phrases.append(' '.join(tokenized))
        else:
            exhibit_augmented_phrases.append(' '.join(tokenized))

    dates_augmented_phrases = []
    for phrase in exhibit_augmented_phrases:
        tokenized = phrase.split()
        if '[DATE]' in tokenized or '[DATE],' in tokenized:
            for i, token in enumerate(tokenized):
                if 'DATE' in token:
                    break
            for day in dates:
                tokenized[i] = day.strftime("%d %b %Y")
                dates_augmented_phrases.append(' '.join(tokenized))
        else:
            dates_augmented_phrases.append(' '.join(tokenized))

    dates_augmented_phrases = list(set(dates_augmented_phrases))

    f = open(output_path, 'w')
    for phrase in dates_augmented_phrases:
        f.write(phrase)
        f.write('\n')


path_to_tix = 'data/tickets_phrases.txt'
path_to_info = 'data/info_phrases.txt'

augment(path_to_tix, 'data/augmented/tix.txt')
augment(path_to_info, 'data/augmented/info.txt')
