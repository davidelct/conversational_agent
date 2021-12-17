"""
This module converts dates uttered by the user into %d %b %Y dates such that
they can be looked up by conversational agent in the database.
We plan to extend this so that we can handle hours as well as days.
"""

__version__ = '0.1'
__author__ = 'Davide L, Ilse M, Stephanie R'

from dateparser import DateDataParser
from dateutil import parser
from dateutil.relativedelta import *
import json

def get_date(input_date):
    """
    Translates an input date referenced by the user to a date corresponding to a 
    database entry.

    @param input_date (string) : date as uttered by the user

    @return output_date (string) : date in database
    """
    input_date = input_date.lower()
    
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
                return output_date.strftime("%d %b %y")
    
    # Then we try to parse the date with dateutil parser,
    # which is good at weekdays
    try:
        output_date = parser.parse(input_date)
        return output_date.strftime("%d %b %y")
    except parser.ParserError:
        # If that fails, use dataparser, 
        # which is good at everything else
        dp_parser = DateDataParser(languages=['en'])
        output_date = dp_parser.get_date_data(input_date).date_obj
        if output_date is not None:
            return output_date.strftime("%d %b %y")
        else:
            raise ValueError('Date inserted is invalid')

def check_date(date, number):
    dict = json.load("data.json")
    if dict[date] >= number:
        return True
    else:
        return False
        
if __name__ == "__main__":
    date = input("When?\n")
    print(get_date(date))