from newsapi import NewsApiClient
from datetime import datetime,timedelta
import requests
from newspaper import Article
from transformers import pipeline
import simplify

def summarize(article):
    summarizer = pipeline("summarization", model="facebook/bart-base")
    summary = summarizer(article, max_length= 80, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def print_article(url):
    article = Article(url)
    article.download()
    article.parse()
    print("Title:", article.title)
    #print("Text:", summarize(str(article.text[:2000])))  # Show first 500 characters of text
    return summarize(str(article.text[:2000]))
    #print("Title:", article.title)
    #print("Text:", summarize(str(article.text[:2000])))  # Show first 500 characters of text

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
    # Print article titles
    
    for article in data.get("articles", []):
        if count>15:
            break

        print("\n")
        print(article["title"])
        #print(print_article(article["url"]))
        count+=1
        #return print_article(article["url"])

#print(output("Trump"))