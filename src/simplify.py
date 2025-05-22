import re
import spacy
from textblob import TextBlob



def preprocess_query(user_query):

    user_query = user_query.lower()
    
        user_query = re.sub(r"[^a-zA-Z0-9\s]", "", user_query)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(user_query)

    keywords = [token.text for token in doc if (token.pos_ in {"NOUN", "ADJ"} or token.pos_ == "PROPN") and not token.is_stop]

    simple_query = " ".join(keywords[:5])
    
    
    return simple_query

