import parsing
import datetime_handling
from random import sample
exhibit_names = ['universe room', 'flooded forest',
                 'antarctic base', 'geological wall', 'sustainable building']
class Intent():
    
    def __init__(self, sentence):
        self.sentence = sentence
        self.entities = parsing.get_entities(sentence, parsing.get_interests(), exhibit_names)

class Tickets(Intent):

    def __init__(self, number = None, exhibition = None):
        super().__init__()
        self.date = datetime_handling.get_date("today")
        self.number = number
        self.exhibition = exhibition
        self.fill_slots()

    def fill_slots(self):
        for ent in self.entities:
            if ent.label_ == "DATE":
                self.date = ent.text
            elif ent.label == "CARDINAL":
                self.number = ent.text
            elif ent.label == "EXHIBITION":
                self.exhibition = ent.text
        
    def empty_slot(self):
        if self.number == None:
            return "number"
        elif self.exhibition == None:
            return "exhibition"
        else: 
            return None           #if none then the code should check the date -if possible, ask if okay -if not ask for date
    
    def response(res_type):
        if res_type == "number":
            sentences = ["How many tickets do you want?", "How many tickets do you want to buy?", " How many tickets do you need?"]
            return sample(sentences, 1)

    def ask_number(self):
        sentences = ["How many tickets do you want?", "How many tickets do you want to buy?", " How many tickets do you need?"]
        return sample(sentences, 1)

    def ask_exhibition(self):
        pass

    def ask_okay(self):
        pass

    def ask_date(self):
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
        

    

    

    
