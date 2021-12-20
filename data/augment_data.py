from datetime import date, timedelta
from dateutil.relativedelta import *
from collections import OrderedDict
from random import sample


def augment(path_to_data, csv_output_path, label, sample_size=0, short=False):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", 
    "nine", "ten"]

    numbers += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    interests = ["universe", "space", "cosmos", "big bang", "evolution", "science", 
        "life", "physics", "earth", "sun", "moon", "mars", "light", "gravity", 
        "matter", "planet", "star", "technology","astronomy","exploration"]

    interests += ["forest", "jungle", "amazon", "plant", "water", "biodiversity", 
        "brazil", "south america", "animal", "climate", "climate change", "river", 
        "evolution","nature"]

    interests += ["artic", "south pole", "north pole", "photos", "ecology", 
        "environment", "photography", "exploration","climate change","biodiversity",
        "climate","nature"]

    interests += ["nature", "volcano", "rock", "landscape", "earthquake", "evolution", 
        "earth","geology","earth"]

    interests += ["sustainability", "education", "efficiency", "architecture", 
        "climate change", "urban planning", "design"]

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

    with open(csv_output_path, "w") as f:
        f.write("phrase,class")
        f.write("\n")
        for sentence in dates_augmented_phrases:
            f.write(sentence +","+ str(label))
            f.write("\n")


def add_dummy_intent():
    phrases = ["one", "two", "three", "four", "five", "six", "seven", "eight", 
    "nine", "ten"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["one", "two", "three", "four", "five", "six", "seven", "eight", 
    "nine", "ten"]

    phrases += ["one", "two", "three", "four", "five", "six", "seven", "eight", 
    "nine", "ten"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["one", "two", "three", "four", "five", "six", "seven", "eight", 
    "nine", "ten"]

    phrases += ["1", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10"]

    phrases += ["universe room", "flooded forest", "antarctic base", 
        "geological wall", "sustainable building"]
    
    phrases += ["universe room", "flooded forest", "antarctic base", 
        "geological wall", "sustainable building"]
    
    phrases += ["universe room", "flooded forest", "antarctic base", 
        "geological wall", "sustainable building"]

    phrases += ["universe room", "flooded forest", "antarctic base", 
        "geological wall", "sustainable building"]
    
    phrases += ["universe room", "flooded forest", "antarctic base", 
        "geological wall", "sustainable building"]

    phrases += ["the universe room", "the flooded forest", "the antarctic base", 
        "the geological wall", "the sustainable building"]

    phrases += ["the universe room", "the flooded forest", "the antarctic base", 
        "the geological wall", "the sustainable building"]

    phrases += ["for the universe room", "for the flooded forest", "for the antarctic base", 
        "for the geological wall", "for the sustainable building"]

    phrases += ["to the universe room", "to the flooded forest", "to the antarctic base", 
        "to the geological wall", "to the sustainable building"]

    interests = ["universe", "space", "cosmos", "big bang", "evolution", "science", 
        "life", "physics", "earth", "sun", "moon", "mars", "light", "gravity", 
        "matter", "planet", "star", "technology","astronomy","exploration"]

    interests += ["forest", "jungle", "amazon", "plant", "water", "biodiversity", 
        "brazil", "south america", "animal", "climate", "climate change", "river", 
            "evolution","nature"]

    interests += ["artic", "south pole", "north pole", "photos", "ecology", 
        "environment", "photography", "exploration","climate change","biodiversity",
        "climate","nature"]

    interests += ["nature", "volcano", "rock", "landscape", "earthquake", "evolution", 
        "earth","geology","earth"]

    interests += ["sustainability", "education", "efficiency", "architecture", 
        "climate change", "urban planning", "design"]

    phrases += interests
    phrases += ["i like " + interest for interest in interests]
    phrases += ["i like " + interest for interest in interests]
    phrases += ["i like " + interest for interest in interests]
    phrases += ["i'm interested in " + interest for interest in interests]
    phrases += ["i love " + interest for interest in interests]
    for _ in range(40):
        two_interests = sample(interests,2)
        string = two_interests[0] + " and " + two_interests[1]
        phrases += [string] 

    for _ in range(40):
        two_interests = sample(interests,2)
        string = "i like " + two_interests[0] + " and " + two_interests[1]
        phrases += [string] 

    for _ in range(40):
        two_interests = sample(interests,2)
        string = "i'm interested in " + two_interests[0] + " and " + two_interests[1]
        phrases += [string]

    for _ in range(40):
        two_interests = sample(interests,2)
        string = "i love " + two_interests[0] + " and " + two_interests[1]
        phrases += [string]

    today = date.today()
    end_date = today + relativedelta(months=+12)
    delta = end_date - today
    dates = [(today + timedelta(days=i)) for i in range(delta.days + 1)]
    db = sample(dates, 50)
    bd = sample(dates, 50)
    phrases += [day.strftime("%d %b") for day in db]
    phrases += [day.strftime("%b %d") for day in bd]
    phrases += ["today", "tomorrow"]
    phrases += ["today", "tomorrow"]
    phrases += ["today", "tomorrow"]
    phrases += ["today", "tomorrow"]
    phrases += ["on Monday", "on Tuesday", "on Wednesday", "on Thursday", 
        "on Friday", "on Saturday", "on Sunday"]
    phrases += ["this Monday", "this Tuesday", "this Wednesday", "this Thursday", 
        "this Friday", "this Saturday", "this Sunday"]
    phrases += ["next Monday", "next Tuesday", "next Wednesday", "next Thursday", 
        "next Friday", "next Saturday", "next Sunday"]
    phrases += ["this week", "next week","this weekend", "next weekend", 
        "this month", "next month"]
    phrases += ["on Monday", "on Tuesday", "on Wednesday", "on Thursday", 
        "on Friday", "on Saturday", "on Sunday"]
    phrases += ["this Monday", "this Tuesday", "this Wednesday", "this Thursday", 
        "this Friday", "this Saturday", "this Sunday"]
    phrases += ["next Monday", "next Tuesday", "next Wednesday", "next Thursday", 
        "next Friday", "next Saturday", "next Sunday"]
    phrases += ["this week", "next week","this weekend", "next weekend", 
        "this month", "next month"]

    f = open("augmented/slot_filling.csv", "w")
    f.write("phrase,class")
    f.write("\n")
    for phrase in phrases:
        string = phrase + "," + str(5)
        f.write(string)
        f.write('\n')

path_to_tix = 'tix.txt'
path_to_interests = 'interests.txt'
path_to_info = 'info.txt'

augment(path_to_tix,'augmented/tix.csv', 0, sample_size = 1, short=True)
augment(path_to_interests,'augmented/interests.csv', 1)
augment(path_to_info,'augmented/info.csv',2, sample_size= 29, short=True)
add_dummy_intent()