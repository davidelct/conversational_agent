import parsing
import datetime_handling
from random import sample
exhibit_names = ['universe room', 'flooded forest',
                 'antarctic base', 'geological wall', 'sustainable building']
class Intent():
    
    def __init__(self):
        self.parameters = []

    def ents_new_sentence(self, sentence):
        self.entities = parsing.get_entities(sentence, parsing.get_interests(), exhibit_names)

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
        for key, value in self.parameters.values():
            if value == None:
                self.prompt(key)
        return self.prompt("DATE")
                             #if none then the code should check the date -if possible, ask if okay -if not ask for date
    
    def prompt(self, slot):
        if slot == "CARDINAL":
            sentences = ["How many tickets do you want?", "How many tickets do you want to buy?", " How many tickets do you need?"]
            return sample(sentences, 1)
        elif slot == "EXHIBITION":
            sentences = ["Sure, Which exhibitions for?", "Perfect, Which exhibition do you want to visit?",  "Great, Do you want it for the general entrance or a specific exhibition?"]
            return sample(sentences, 1)
        elif slot == "DATE":
            self.available = datetime_handling.check_date(self.parameters["DATE"], self.parameters["NUMBER"])
            if self.available == False:
                sentences = ["So sorry we have no tickets for", self.parameters["DATE"],  ", another day maybe?", "Sorry tickets for ", self.parameters["DATE"],  " run out, what other day suits you?", "Sorry, ", self.parameters["DATE"],  " we are not available for your visit, could you tell me another day?"]
                return sample(sentences, 1)
                
    def response(res_type):
        pass

    

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
        

    

    

    
