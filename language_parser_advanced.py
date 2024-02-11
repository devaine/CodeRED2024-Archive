import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def extract_locations(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Tag parts of speech
    pos_tags = pos_tag(tokens)
    # Perform named entity recognition
    named_entities = ne_chunk(pos_tags)
    # Extract locations
    locations = [entity for entity in named_entities if isinstance(entity, nltk.Tree) and entity.label() == 'GPE']
    return [' '.join([child[0] for child in location]) for location in locations]


sentence = "Welcome to the US"
ensw = stopwords.words('english')
token = nltk.word_tokenize(sentence)
filterArr = [ item for item in token if item not in ensw]
named_entities = ne_chunk()


# def extract(text):
