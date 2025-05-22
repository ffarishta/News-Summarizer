import re
import spacy
from textblob import TextBlob



def preprocess_query(user_query):
    # Convert to lowercase
    user_query = user_query.lower()
    
    # Remove special characters
    user_query = re.sub(r"[^a-zA-Z0-9\s]", "", user_query)

    #new_query = []
    #for i in user_query.split():
    #    corrected = str(TextBlob(i).correct())
    #    new_query.append(corrected)
    #new_query = " ".join(new_query)
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(user_query)

    # Extract meaningful keywords (nouns, proper nouns, and adjectives)
    keywords = [token.text for token in doc if (token.pos_ in {"NOUN", "ADJ"} or token.pos_ == "PROPN") and not token.is_stop]

    # Limit to top 5 keywords
    simple_query = " ".join(keywords[:5])
    
    
    return simple_query

#user_input ="How is CRISPR technology revolutionizing genetic engineering?"
#processed_query = preprocess_query(user_input)

#print(processed_query)
