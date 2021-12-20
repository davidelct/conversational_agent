from random import sample
from numpy import maximum
import spacy
import json
from word2number import w2n
from dateparser import DateDataParser
from dateutil import parser
from dateutil.relativedelta import *
  
class ProvideInfo:

    def __init__(self):
        data_file_tickets = open("data/tickets_data.json")
        self.data_tickets = json.load(data_file_tickets)
        data_file_exhibits = open("data/exhibits_data.json")
        self.data_exhibits = json.load(data_file_exhibits)
        self.classifier = spacy.load("en_core_web_sm")

        self.exhibits = ['universe room', 
            'flooded forest', 
            'antarctic base', 
            'geological wall', 
            'sustainable building'
        ]
        self.date = None
        self.exhibit = None
        self.query = None
        self.answer_ids =   {
                            "1": 
                                {"question": "I want to know which exhibitions the museum has", 
                                "parameters": "None"},
                            "2": {"question": "Are there exhibitions for kids?",
                                "parameters": "None"},
                            "3": {"question": "Is the museum open on date?",
                                "parameters": "DATE"},
                            "4": {"question": "What is this exhibition about?",
                                "parameters": "EXHIBIT"},
                            "5": {"question": "Who worked on this exhibition?",
                                "parameters": "EXHIBIT"}
                            }
        self.parameters_needed = None
      
    def add_entities(self, entities):
        for entity in entities:
            if entity.label_ == "DATE":
                self.date = entity
            elif entity.label_ == "EXHIBIT":
                self.exhibit = entity

    def get_date(self):
        input_date = self.date.text.lower()
        
        weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday", 
        "saturday", "sunday")

        # We first handle dates like "this friday", "next friday", "on friday"
        for day in weekdays:
            if day in input_date:
                if "this" in input_date:
                    input_date = day
                elif "next" in input_date:
                    this = parser.parse(day)
                    output_date = this + relativedelta(weeks=+1)
                    return output_date.strftime("%d %b")
        
        # Then we try to parse the date with dateutil parser,
        # which is good at weekdays
        try:
            output_date = parser.parse(input_date)
            return output_date.strftime("%d %b")
        except parser.ParserError:
            # If that fails, use dataparser, 
            # which is good at everything else
            dp_parser = DateDataParser(languages=['en'])
            output_date = dp_parser.get_date_data(input_date).date_obj
            if output_date is not None:
                return output_date.strftime("%d %b")
            else:
                raise ValueError('Date inserted is invalid')

    def get_exhibit(self):
        if self.exhibit.text.lower() in self.exhibits:
            return self.exhibit.text.lower()
        else:
            return None

    def missing_info(self):
        if self.parameters_needed == "None":
            return False
        if self.parameters_needed == "EXHIBIT":
            return self.exhibit == None
        if self.parameters_needed == "DATE":
            return self.date == None

    def prompt(self, parameter):
        prompts = {
            "date": ["When would you like to go?", "Which day?",
                "For what day?"],
            "exhibit": ["Which exhibition would you like to know more about?", "For which exhibition?"]
        }
        if self.parameters_needed == "DATE" and self.date == None:
            parameter = "date"
        elif self.parameters_needed == "EXHIBIT" and self.exhibit == None:
            parameter = "exhibit"
        return sample(prompts[parameter], 1)[0]

    def get_entities(self):
        entities = []
        if self.date != None:
            entities.append(self.date)
        if self.exhibit != None:
            entities.append(self.exhibit)
        return entities

    def museum_open(self):
        return int(self.data_tickets[self.date]) >= 1

    def classify_question(self, question):
        q = self.classifier(question)
        similarity_scores = []
        for i in range(5):
            similarity_scores.append(q.similarity(self.classifier(self.answer_ids[i+1]["question"])))
        max_index = similarity_scores.index(max(similarity_scores))
        self.query = self.answer_ids[max_index]
        self.parameters_needed = self.answer_ids[max_index]["parameters"]
    
    def respond(self, output_file):
        if self.query == "Is the museum open on date?":
            response = "If I understand correctly, you want to know if the museum is open on " + str(self.get_date()) + "?"
            error = False
        if self.query == "What is this exhibition about?":
            response = "If I understand correctly, you want to know what the " + str(self.get_exhibit()) + " exhibition is about?"
            error = False
        if self.query == "Who worked on this exhibition?":
            response = "If I understand correctly, you want to know who worked on the " + str(self.get_exhibit()) + " exhibition?"
            error = False
        if self.query == "Are there exhibitions for kids?":
            response = "If I understand correctly, you want to know if the museum is suitable for kids?"
            error = False
        if self.query == "I want to know which exhibitions the museum has":
            response = "If I understand correctly, you want to know which exhibitions the museum has?"
            error = False
        return response, error

    def action(self, output_file):
        response = []
        if self.query == "Is the museum open on date?":
            if self.museum_open():
                response.append("The whole museum is open on " + str(self.get_date()) + ", so also the " + str(self.get_exhibit()) + ".")
            else: 
                response.append("Unfortunately there are no tickets available on " + str(self.get_date()) + ". Remember that our museum is closed on mondays!")
        if self.query == "What is this exhibition about?":
            response.append(self.data_exhibits[self.get_exhibit()]["description"])
        if self.query == "Who worked on this exhibition?":
            response.append(self.data_exhibits[self.get_exhibit()]["curator"])
        if self.query == "Are there exhibitions for kids?":
            response.append("The museum is a beautiful place for all the members of the family to enjoy learning while playing")
        if self.query == "I want to know which exhibitions the museum has":
            response.append("The museum has five permanent exhibitions: the flooded forest, the universe room, the antartic base, the geologic wall and the sustainable building")
        return response
