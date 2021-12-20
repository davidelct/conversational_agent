from word2number import w2n
from dateparser import DateDataParser
from dateutil import parser
from dateutil.relativedelta import *

class Welcome():

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
        self.interests = []

    def add_entities(self, entities):
        for entity in entities:
            if entity.label_ == "CARDINAL":
                self.no_tickets = entity
            elif entity.label_ == "DATE":
                self.date = entity
            elif entity.label_ == "EXHIBIT":
                self.exhibit = entity
            elif entity.label_ == "INTEREST":
                self.interests.append(entity)

    def get_exhibit(self):
        if self.exhibit.text.lower() in self.exhibits:
            return self.exhibit.text.lower()
        else:
            return None

    def get_number(self):
        try:
            return int(self.no_tickets.text)
        except ValueError:
            return w2n.word_to_num(self.no_tickets.text)
    
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
    
    def get_entities(self):
        entities = []
        if self.no_tickets != None: 
            entities.append(self.no_tickets)
        if self.date != None:
            entities.append(self.date)
        if self.exhibit != None:
            entities.append(self.exhibit)
        for interest in self.interests:
            entities.append(interest)
        return entities

    def respond(self):
        response = "Hello, I can help you by purchasing tickets, recommending exhibitions or providing general information about the museum."
        error = True
        self.complete = True
        return response, error