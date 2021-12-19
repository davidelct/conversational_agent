from ner import parse
from random import sample
import json
from communication import ask,say
from intent_classifier import get_intent

class RecommendExhibit:

    def __init__(self):
        data_file = open("data/exhibits_data.json")
        self.data = json.load(data_file)

        self.interests = []
        self.matched_exhibits = []
    
    def new_sentence(self, sentence):
        entities = parse(sentence)
        self.fill_slots(entities)

    def fill_slots(self, entities):
        for entity in entities:
            if entity.label_ == "INTEREST":
                self.interests.append(entity.text)
        if self.empty_slots():
            self.fill_empty_slots()
        else:
            self.action()

    def empty_slots(self):
        return len(self.interests) == 0

    def request(self):
        prompts = ["What are you interested in?", "What's your passion?", "What do you like?"]
        sentence = ask(sample(prompts, 1)[0])
        self.new_sentence(sentence)

    def fill_empty_slots(self):
        while self.empty_slots():
            self.request()

    def find_match(self):
        counters = {}
        for exhibit in self.data.keys():
            counter = 0
            for interest in self.interests:
                if interest in self.data[exhibit]["interests"]:
                    counter += 1
            counters[exhibit] = counter

        matches = []
        for exhibit,counter in counters.items():
            matches.append((exhibit,counter))
        matches.sort(key=lambda x:x[1],reverse=True)
        print(matches)
        top_matches = []
        if matches[0][1] > 0:
            top_matches.append(matches[0][0])
            if matches[1][1] > 0:
                top_matches.append(matches[1][0])
        self.matched_exhibits = top_matches

    def action(self):
        self.find_match()
        print(self.matched_exhibits)
        if len(self.matched_exhibits):
            sentence = "Awesome! Based on your interest in " + self.interests[0]
            if len(self.interests) > 1:
                for interest in self.interests[1:-1]:
                    sentence += ", " + interest
                sentence += " and " + self.interests[-1]
            sentence += " I think you should check out our " + self.matched_exhibits[0]
            if len(self.matched_exhibits) > 1:
                sentence += " and " + self.matched_exhibits[1] + " exhibitions. Would you like to hear more about them?"       
            else:
                sentence += " exhibition. Would you like to hear more about it?"
            response = ask(sentence)
            if response == "yes":
                self.describe_exhibits()
        else:
            sentence = "Sorry, it seems like we don't have anything matching your interests at the moment."
            say(sentence)
        
    def describe_exhibits(self):
        for exhibit in self.matched_exhibits:
            say(self.data[exhibit]["description"])   

query = ask("Hello, my name is Cosmo. How can I help you?")
intent = get_intent(query)
if intent == "interests":
    intent = RecommendExhibit()
    intent.new_sentence(query)