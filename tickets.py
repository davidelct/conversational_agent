from ner import parse
from random import sample
from datetime_handling import get_date
import json
from asr import ask,say
from intent_classifier import get_intent
from word2number import w2n
import intent

def str_to_intent(label):
    if label == "tix":
        return(intent.Tickets())
    if label == "interest":
        return(intent.Interest())
    if label == "info":
        return(intent.Info())
    if label == "welcome":
        return(intent.Welcome())
    else:
        return(intent.Fallback())

class PurchaseTickets:

    def __init__(self):
        data_file = open("tickets_data.json")
        self.data = json.load(data_file)

        self.exhibits = ['universe room', 
            'flooded forest', 
            'antarctic base', 
            'geological wall', 
            'sustainable building'
        ]
        self.no_tickets = None
        self.date = None
        self.exhibit = None
    
    def new_sentence(self, sentence):
        new_intent = get_intent(sentence)
        if new_intent not in intents:
            if new_intent == "interest":
                answer = ask("I can give you a recommendation for exhibits based on your interests, would this be something you're interested in?")
                if answer == "yes":
                    intents.append(new_intent)
                    str_to_intent(intents[len(intents)-1]).new_sentence(sentence)
            if new_intent == "info":
                ask("Do you want more information about certain exhibits or the museum before continuing?")
                if answer == "yes":
                    intents.append(new_intent)
                    str_to_intent(intents[len(intents)-1]).new_sentence(sentence)
        entities = parse(sentence)
        self.fill_slots(entities)

    def fill_slots(self, entities):
        for entity in entities:
            if entity.label_ == "CARDINAL":
                self.no_tickets = self.get_number(entity.text)
            elif entity.label_ == "DATE":
                self.date = get_date(entity.text)
            elif entity.label_ == "EXHIBIT":
                self.exhibit = self.get_exhibit(entity.text)
        if self.empty_slots():
            self.fill_empty_slots()
        else:
            self.action()

    def get_exhibit(self, exhibit):
        if exhibit.lower() in self.exhibits:
            return exhibit.lower()
        else:
            say("Sorry, I don't know which exhibit you mean.")
            return None

    def get_number(self, number):
        try:
            num = int(number)
        except ValueError:
            try:
                num = w2n.word_to_num(number)
            except ValueError:
                say("Sorry, that's not a valid number.")
                num = None
        return num


    def empty_slots(self):
        return (self.no_tickets == None 
            or self.date == None 
            or self.exhibit == None)

    def request(self, parameter):
        prompts = {
            "no_tickets" : ["How many tickets would you like?", "How many tickets?", 
                "How many tickets do you need?"],
            "date": ["When would you like to go?", "For what day should I reserve your tickets?",
                "For what day?"],
            "exhibit": ["Which exhibition would you like to go to?", "For which exhibition?"]
        }
        sentence = ask(sample(prompts[parameter], 1)[0])
        self.new_sentence(sentence)

    def fill_empty_slots(self):
        while self.empty_slots():
            if self.no_tickets == None:
                self.request("no_tickets")
            if self.date == None:
                self.request("date")
            if self.exhibit == None:
                self.request("exhibit")

    def ticket_available(self):
        return int(self.data[self.date]) >= int(self.no_tickets)

    def action(self):
        if self.exhibit.lower() in self.exhibits:
            if self.ticket_available():
                sentence = str(self.no_tickets) + " ticket"
                if self.no_tickets > 1:
                    sentence += "s"
                sentence += " on " + self.date + " for " + self.exhibit
                sentence += ". That will be " + str(6*self.no_tickets) + " euros."
                sentence += " Would you like to proceed?"
                response = ask(sentence)
                if response == 'yes':
                    sentence = "Ok, here is your ticket"
                    if self.no_tickets > 1:
                        sentence = "Ok, here are your tickets"
                    
                    say(sentence)
                else:
                    say("Ok, I canceled the order.")
            else:
                sentence = "Sorry, we are sold out on " + self.date
                say(sentence)
                sentence = "Would you like to book for another day?"
                response = ask(sentence)
                if response == 'yes':
                    self.request("date")
                elif response != 'yes' and response != 'no':
                    self.new_sentence(response)
        else:
            sentence = "I'm sorry, we don't have an exhibition named " + self.exhibit
            say(sentence)

query = ask("Hello, my name is Cosmo. How can I help you?")
intent_ = get_intent(query)
intents = []
intents.append(intent_)

for intent_ in intents:
    str_to_intent(intent).new_sentence(query)
