from nltk import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import contractions
from dateparser import DateDataParser
from dateutil import parser
from dateutil.relativedelta import *
import json

def clean_text(text):
    text = contractions.fix(text)
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    text = text.split()
    text = [w for w in text if not w in stop_words]
    text = " ".join(text)
    text = WordPunctTokenizer().tokenize(text)
    lemm = WordNetLemmatizer()
    text = [lemm.lemmatize(w) for w in text]
    text = " ".join(text)
    return text

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

def check_date(date, number):
    f = open("data.json", 'r')
    dict = json.load(f)
    date = get_date(date)
    if int(dict[date]) >= int(number):
        return True
    else:
        return False