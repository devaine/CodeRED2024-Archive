# Currently unfinished
""" To be implemented, run these commands first:
source venv/bin/activate
pip install nltk
"""

import nltk
import re
import csv

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
nltk.download('punkt')
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk


def remove_stopwords(text):
    ensw = stopwords.words('english')
    token = nltk.word_tokenize(text)
    filterArr = [ item for item in token if item not in ensw]
    return filterArr

def extract_origin(text):
    with open('worldcities.csv','r',errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)

        
        for line in csv_reader:
            if(line[0].upper() in text.upper()):
                return line[0]
    
    return "no city found"
                
    

def extract_destination(text):
    tokenized = word_tokenize(text)
    origin = tokenized[tokenized.index('to')+1]
    return origin

def extract_date(text):
    # Proper Format
    date_formated = re.findall(r'\d+\S\d+\S\d+', text)
    if(date_formated is not -1):
        return date_formated[0]
    # Month Format bbb
    m = ""
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    tokenized = remove_stopwords(text)
    index = 1
    for month in months:
        if month in tokenized:
            m = index
        index += 1
    
def extract_adults(text):
    # Literally says 2 adults
    if re.findall(r'\b(adult|adults)\b', text) is -1:
        return 1
    adult_or_adults = re.findall(r'\b(adult|adults)\b', text)[0]
    tokenized = word_tokenize(text)
    adult_count = tokenized[tokenized.index(adult_or_adults)-1]
    return adult_or_adults
    # if(adult_count is not -1):
    #     return adult_count [0]
def extract_adults(text):
    # Tokenize the string
    tokens = word_tokenize(text)

    # Part-of-speech tag the tokens
    pos_tags = pos_tag(tokens)

    # Perform named entity recognition
    named_entities = ne_chunk(pos_tags)

    # Extract the number of people
    people_count = sum(1 for subtree in named_entities.subtrees() if subtree.label() == 'PERSON')

    print(f"Number of people in the string: {people_count}")

def extract_country(origin):
    country=""
    with open('worldcities.csv','r',errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)

        
        for line in csv_reader:
            if(line[0].upper()==origin.upper()):
                country=line[4].upper()
                return country
    return "no country found"

def extract_currency(country):
    currency=""
    with open('codes-all.csv','r',errors='ignore') as csv_file:
        
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            if(line[0].upper()==country.upper()):
                currency=line[2].upper()
                return currency
            
    return "USD"

    

        


sentence = "from Rio De Janeiro to Canada on 1/1/70 with two men and one women"
#sentence = "Flights from Boston to Madrid from June 7th to June 14th"

#origin=extract_origin(sentence)
#print(origin)
#print(extract_origin(origin))
#print(extract_date(sentence))
#print(extract_adults(sentence))
#extract_adults(sentence)
print(extract_origin(sentence))
print(extract_currency(extract_country(extract_origin(sentence))))