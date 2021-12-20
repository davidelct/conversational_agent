from pickle import NONE
from nlu_units.ner import parse
from utils import get_date, check_date
from random import sample
from communication import say, ask
import word2number as w2n
exhibit_names = ['universe room', 'flooded forest',
                 'antarctic base', 'geological wall', 'sustainable building']

class Welcome:

    def __init__(self):
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

    def action(self):
        ask("Hello, what can I do for you today?")

class Welcome:

    def __init__(self):
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

    def action(self):
        ask("I am sorry, I was not able to execute your request, what can I do for you today?")

class Intent():
    
    def __init__(self):
        self.parameters = []

    def ents_new_sentence(self, sentence):
        self.entities = parse(sentence)

class Tickets(Intent):

    def __init__(self, date = get_date("today"), number = None, exhibition = None):
        super().__init__()
        self.parameters = {"DATE": date, "CARDINAL": number, "EXHIBITION": exhibition}
        self.available = None

    def ents_new_sentence(self, sentence):
        self.entities = parse(sentence)
        self.fill_slots()

    def fill_slots(self):
        for ent in self.entities:
            for label in self.parameters.keys():
                if ent.label_ == label:
                    self.parameters[label] = ent.text
        
    def empty_slot(self):
        for key in self.parameters:
            if self.parameters[key] == None:
                return(self.prompt(key))
        for key in self.parameters:
            if self.parameters[key] == None:
                self.empty_slot()
        return None
                             #if none then the code should check the date -if possible, ask if okay -if not ask for date
    def ticket_available(self):
        return check_date(self.parameters["DATE"], self.parameters["CARDINAL"])

    def prompt(self, slot):
        if slot == "CARDINAL":
            sentences = ["How many tickets do you want?", "How many tickets do you want to buy?", " How many tickets do you need?"]
            return sample(sentences, 1)
        elif slot == "EXHIBITION":
            sentences = ["Sure, Which exhibitions for?", "Perfect, Which exhibition do you want to visit?",  "Great, Do you want it for the general entrance or a specific exhibition?"]
            return sample(sentences, 1)
        elif slot == "NOT_AVAIL":
            sentences = ["So sorry we have no tickets for" + str(self.parameters["DATE"]) +  ", another day maybe?", "Sorry tickets for " + str(self.parameters["DATE"]) +  " run out, what other day suits you?", "Sorry, " + str(self.parameters["DATE"]) +  " we are not available for your visit, could you tell me another day?"]
            return sample(sentences, 1)
        elif slot == "FULL":
            sentences = ["Am I correct that you want to buy " + str(self.parameters["CARDINAL"]) + " tickets for the exhibition " + str(self.parameters["EXHIBITION"]) + " for " + str(self.parameters["DATE"]) + "? Respons with YES or NO please."]
            return sample(sentences, 1)
        else: return "fault"
                
    def response(self, confirm):
        if confirm.lower() == "yes":
            return "Here is your ticket!"
        elif confirm.lower() == "no":
            return "Please tell me what the information should be."
class Welcome(Intent):

    def __init__(self, date = get_date("today"), number = None, exhibition = None, interest = None):
        super().__init__()
        self.parameters = {"DATE": date, "CARDINAL": number, "EXHIBITION": exhibition, "INTEREST": interest}

    def ents_new_sentence(self, sentence):
        self.entities = parse(sentence)
        self.fill_slots()

    def fill_slots(self):
        for ent in self.entities:
            for label in self.parameters.keys():
                if ent.label_ == label:
                    self.parameters[label] = ent.text
        
    def empty_slot(self):
        return None
                             #if none then the code should check the date -if possible, ask if okay -if not ask for date
    def prompt(self, slot):
        if slot == "FULL":
            return "yes"
        else: return "fault"
                
    def response(self, confirm):
        if confirm.lower() == "yes":
            return "Hello, what can I do for you today?"
    
class Fallback(Intent):
    def __init__(self, date = datetime_handling.get_date("today"), number = None, exhibition = None, interest = None):
        super().__init__()
        self.parameters = {"DATE": date, "CARDINAL": number, "EXHIBITION": exhibition, "INTEREST": interest}

    def ents_new_sentence(self, sentence):
        self.entities = parse(sentence)
        self.fill_slots()

    def fill_slots(self):
        for ent in self.entities:
            for label in self.parameters.keys():
                if ent.label_ == label:
                    self.parameters[label] = ent.text
        
    def empty_slot(self):
        return None
                             #if none then the code should check the date -if possible, ask if okay -if not ask for date
    def prompt(self, slot):
        if slot == "FULL":
            return "yes"
        else: return "fault"
                
    def response(self, confirm):
        if confirm.lower() == "yes":
            return "Sorry I didn't understand that, what can I do for you today?"

"""
class Info(Intent):

    def __init__(self, exhibition = None):
        super().__init__()
        self.date = datetime_handling.get_date("today")
        self.exhibition = exhibition
        self.fill_slots()

    def fill_slots(self):
        for ent in self.entities:
            if ent.label_ == "DATE":
                self.date = ent.text
            elif ent.label == "EXHIBITION":
                self.exhibition = ent.text
        if self.exhibition == None:
            self.ask_exhibition()
        
class Interest(Intent):

    def __init__(self, interest = None, exhibition = None):
        super().__init__()
        self.date = datetime_handling.get_date("today")
        self.exhibition = exhibition
        self.interest = interest
        self.fill_slots()

    def fill_slots(self):
        for ent in self.entities:
            if ent.label_ == "DATE":
                self.date = ent.text
            elif ent.label == "EXHIBITION":
                self.exhibition = ent.text
            elif ent.label == "INTEREST":
                self.interest = ent.text
        if self.number == None:
            self.ask_number()
        if self.exhibition == None:
            self.ask_exhibition()


"""
        

    

    

    
