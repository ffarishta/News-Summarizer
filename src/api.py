from newsapi import NewsApiClient
from datetime import datetime,timedelta
import requests
from newspaper import Article
from transformers import pipeline
import simplify
import re
from urllib.parse import urlparse


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(article):
    article = clean_text(article)
    summary = summarizer(article, max_length=1000, min_length=60, do_sample=False, num_beams=4)
    return summary[0]['summary_text']

def clean_text(text):
    text = re.sub(r"(Share\s+Save|Listen to.*?article|[A-Z][a-z]+\s+[A-Z][a-z]+,?\s+(Editor|Reporter).*)", "", text)
    text = re.sub(r"\d{1,2}\s+\w+\s+\d{4}", "", text)  # remove dates like 24 April 2025
    return text.strip()

def print_article(url):
    article = Article(url)
    article.download()
    article.parse()
    #print("Title:", article.title)
    title = article.title
    print(article.text)
    summary = summarize(str(article.text))
    return (title,summary)

def output(inp):
    api_key = "0a359618697c4231a43d45282a597e08"

    BASE_URL = "https://newsapi.org/v2/everything"
    #inp = ""

    #while inp != "exit":
        #inp = input("Enter Some Phrase: ")

    query = simplify.preprocess_query(inp)
    
    print(query)

    encoded_query = query.replace(" ", "%")  # Encoding spaces as '+'

    trusted_domains = [
        "bbc.com", "cnn.com", "theguardian.com", "nytimes.com", "reuters.com",
        "wsj.com", "bloomberg.com", "forbes.com", "abcnews.go.com", "cbsnews.com",
        "nbcnews.com", "usatoday.com", "washingtonpost.com", "theverge.com", "vox.com",
        "apnews.com", "aljazeera.com", "france24.com", "dw.com", "sky.com",
        "thehill.com", "businessinsider.com", "bbc.co.uk", "latimes.com", "economist.com",
        "time.com", "thelocal.se", "lemonde.fr", "guardian.co.uk", "thetimes.co.uk",
        "indiatoday.in", "stripes.com", "newyorker.com", "sfgate.com", "globalnews.ca",
        "dailymail.co.uk", "thefinancialexpress.com", "chinadaily.com.cn", "rt.com", "theatlantic.com",
        "npr.org", "huffpost.com", "thewrap.com", "newsweek.com", "motherjones.com",
        "fivethirtyeight.com", "propublica.org", "theguardian.co.uk", "vox.com", "talkingpointsmemo.com",
        "thedailybeast.com", "businessweek.com", "newyorktimes.com", "independent.co.uk", "cbc.ca"
    ]

    params = {
        "q": encoded_query,  # Search query
        "domains": trusted_domains, 
        "language": "en",    # Retrieve only English articles
        "sortBy": "relevancy",  # Sort by latest articles
        "apiKey": api_key
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    count = 0
    articles = {}
    count = 0
    for article in data.get("articles", []):
        url = article["url"]
        x,y = print_article(url)
        articles[x] = [y,url, urlparse(url).netloc]
        if count > 1:
            break
        count += 1
        
    
    return articles
      

#print(output("Climate"))