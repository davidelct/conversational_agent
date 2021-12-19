import spacy
from ner import parse
from random import sample
from utils import get_date
import json
from communication import ask,say
from intent_classifier import get_intent

nlp=spacy.load('en_core_web_sm')
  
class GiveInformation:

    def __init__(self):
        data_file = open("exhibits_data.json")
        self.data = json.load(data_file)

        self.exhibits = ['universe room', 
            'flooded forest', 
            'antarctic base', 
            'geological wall', 
            'sustainable building'
        ]
        self.date = None
        self.exhibit = None
        self.query = None
    
    def new_sentence(self, sentence):
        entities = parse(sentence)
        self.fill_slots(entities)

    def fill_slots(self, entities):
        for entity in entities:
            if entity.label_ == "DATE":
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

    def empty_slots(self):
        return (self.date == None 
            or self.exhibit == None)

    def request(self, parameter):
        prompts = {
            "date": ["When would you like to go?", "Which day?",
                "For what day?"],
            "exhibit": ["Which exhibition would you like to know more about?", "For which exhibition?"]
        }
        sentence = ask(sample(prompts[parameter], 1)[0])
        self.new_sentence(sentence)

    def fill_empty_slots(self):
        while self.empty_slots():
            if self.date == None:
                self.request("date")
            if self.exhibit == None:
                self.request("exhibit")

    def museum_open(self):
        return int(self.data[self.date]) >= 1

    def classify_question(self, question):
        q = nlp(question)
        questions = ["I want to know which exhibitions the museum has","Are there exhibitions for kids?","Is the museum open on date?",
                    "What is this exhibition about?", "Who worked on this exhibition?"]
        similarity_scores = []
        for q_ in questions:
            similarity_scores.append(q.similarity(nlp(q_)))
        max_index = similarity_scores.index(max(similarity_scores))
        self.query = questions[max_index]
        
    def action(self):
        if self.query == "Is the museum open on date?":
            if self.museum_open():
                say("The whole museum is open on " + str(self.date) + ", so also the " + str(self.exhibit)) + "."
            else:
                say("Unfortunately there are no tickets available on " + str(self.date) + " remember that our museum is closed on mondays!")
        if self.query == "What is this exhibition about?":
            say(self.data[self.exhibit]["description"])  
        if self.query == "Who worked on this exhibition?":
            say(self.data[self.exhibit]["curator"])  

question = ask("Hello, my name is Cosmo. How can I help you?")
intent = get_intent(question)
if intent == "info":
    intent = GiveInformation()
    intent.classify_question(question)
    if intent.query == "Are there exhibitions for kids?":
        say("The museum is a beautiful place for all the members of the family to enjoy learning while playing")
        ''' grounding:
        response = ask("If I understand correctly you want to know if there are exhibitions for kids?")
        if response == "yes":
            say("The museum is a beautiful place for all the members of the family to enjoy learning while playing")
        if response == "no":
            response = ask("Can you repeat the question?")
            intent.classify_question(response)'''
    if intent.query == "I want to know which exhibitions the museum has":
        say("The museum has five permanent exhibitions: the flooded forest, the universe room, the antartic base, the geologic wall and the sustainable building")
    else: intent.new_sentence(question)