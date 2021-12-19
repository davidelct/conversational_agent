from ner import parse
import datetime_handling
from random import sample
exhibit_names = ['universe room', 'flooded forest',
                 'antarctic base', 'geological wall', 'sustainable building']
class Intent():
    
    def __init__(self):
        self.parameters = []

    def ents_new_sentence(self, sentence):
        self.entities = parse(sentence)

class Tickets(Intent):

    def __init__(self):
        super().__init__()
        self.parameters = {"DATE": datetime_handling.get_date("today"), "CARDINAL": None, "EXHIBITION": None}
        self.available = None

    def ents_new_sentence(self, sentence):
        self.entities = parsing.get_entities(sentence, parsing.get_interests(), exhibit_names)
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
        return None
                             #if none then the code should check the date -if possible, ask if okay -if not ask for date
    def ticket_available(self):
        return datetime_handling.check_date(self.parameters["DATE"], self.parameters["CARDINAL"])

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
        

    

    

    
