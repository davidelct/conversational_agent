from ner import parse
from utils import get_date
from communication import ask, say
import word2number as w2n

class Fallback():

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
        ask("I am sorry, I was not able to execute your request")
