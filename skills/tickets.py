from random import sample
import json
from word2number import w2n
from dateparser import DateDataParser
from dateutil import parser
from dateutil.relativedelta import *

class PurchaseTickets:

    def __init__(self):
        data_file = open("data/tickets_data.json")
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
        self.empty_slots = self.missing_info()

    def add_entities(self, entities):
        for entity in entities:
            if entity.label_ == "CARDINAL":
                self.no_tickets = entity
            elif entity.label_ == "DATE":
                self.date = entity
            elif entity.label_ == "EXHIBIT":
                self.exhibit = entity

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

    def get_exhibit(self):
        if self.exhibit.text.lower() in self.exhibits:
            return self.exhibit.text.lower()
        else:
            return None

    def missing_info(self):
        return (self.no_tickets == None 
            or self.date == None 
            or self.exhibit == None)

    def prompt(self):
        prompts = {
            "no_tickets" : ["How many tickets would you like?", "How many tickets?", 
                "How many tickets do you need?"],
            "date": ["When would you like to go?", "For what day should I reserve your tickets?",
                "For what day?"],
            "exhibit": ["Which exhibition would you like to go to?", "For which exhibition?"]
        }
        if self.no_tickets == None:
            parameter = "no_tickets"
        elif self.date == None:
            parameter = "date"
        elif self.exhibit == None:
            parameter = "exhibit"
        return sample(prompts[parameter], 1)[0]

    def get_entities(self):
        entities = []
        if self.no_tickets != None: 
            entities.append(self.no_tickets)
        if self.date != None:
            entities.append(self.date)
        if self.exhibit != None:
            entities.append(self.exhibit)
        return entities

    def ticket_available(self):
        return int(self.data[self.get_date()]) >= int(self.get_number())

    def respond(self, output_file):
        if self.get_exhibit() in self.exhibits:
            if self.ticket_available():
                response = str(self.get_number()) + " ticket"
                if self.get_number() > 1:
                    response += "s"
                response += " on " + self.get_date() + " for " + self.get_exhibit()
                response += ". That will be " + str(6*self.get_number()) + " euros."
                response += " Would you like to proceed?"
                error = False
            else:
                response = "Sorry, we are sold out on " + self.get_date()
                error = True
        else:
            response = "I'm sorry, we don't have an exhibition named " + self.get_exhibit()
            error = True

        return response, error

    def action(self):
        response = []
        if self.get_number() > 1:
            response.append("Ok, here are your " + str(self.get_number()) + " tickets")
        else:
            response.append("Ok, here is your ticket")
        return response         