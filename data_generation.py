"""
This module handles availability data generation for our conversational agent.
Fake data is generated and stored in json format.
We plan to change this module into a data scraper to get real availabilities.
"""

__version__ = '0.1'
__author__ = 'Davide L, Ilse M, Stephanie R'

import random
import json
from datetime import date, timedelta
from dateutil.relativedelta import *
from dateutil import parser

def generate_data(today):
    """
    Generates fake availability data for a 2-month period starting from today.
    The data is then stored in a file named "data.json".

    @param today (datetime.date) today's date
    """
    end_date = today + relativedelta(months=+2)
    delta = end_date - today
    days = [(today + timedelta(days=i)) for i in range(delta.days + 1)]

    data = {}
    for i in range(len(days)):
        key = days[i].strftime("%d %b %Y")
        if days[i].weekday() == 0: # if Monday
            data[key] = 0
        else:
            data[key] = random.randint(0,800)
    datafile = open("data.json", "w")
    json.dump(data, datafile)

if __name__ == "__main__":
    generate_data(date.today())
