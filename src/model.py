from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
article = "Russia and Ukraine are trading blame for continued air attacks on civilian targets in Ukrainian regions Sumy and Donetsk and on energy targets in Russia’s Krasnodar since Russian President Vladimir Putin agreed to a 30-day halt on attacks on energy infrastructure targets in Ukraine following a phone call with United States President Donald Trump on Tuesday.So will the halt on energy attacks be the first step to securing peace in Ukraine, or was it merely a stalling tactic to let the war drag on? Here is what we know so far."
summary = summarizer(article, max_length=20, min_length=10, do_sample=False)
print(summary[0]['summary_text'])