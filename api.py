from fastapi import FastAPI
import re
import nltk
from nltk.corpus import stopwords
import pandas as pd

# Downloading NLTK resources
nltk.download('stopwords')

def cleanhtml(sentence): #function to clean the word of any html-tags
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', sentence)
    return cleantext

def cleanpunc(sentence): #function to clean the word of any punctuation or special characters
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    return  cleaned

def text_cleaning(text: str):
    sno = nltk.stem.SnowballStemmer('english') #initialising the snowball stemmer
    stop = set(stopwords.words('english'))

    sent = cleanhtml(text) # remove HTMl tags
    filtered_sentence = []
    for w in sent.split():
        for cleaned_words in cleanpunc(w).split():
            if cleaned_words.isalpha() and len(cleaned_words) > 2:
                if cleaned_words.lower() not in stop:
                    s = sno.stem(cleaned_words.lower()).encode('utf8')
                    filtered_sentence.append(s)
                else:
                    continue
            else:
                continue

    final_string = b" ".join(filtered_sentence) #final string of cleaned words
    return pd.Series(final_string.decode('utf8'))

app = FastAPI()

@app.post("/data")
async def first():
    return {"message": "hello world"}


@app.post("/clean")
async def clean_text(text: str):
    return {"cleaned_text": text_cleaning(text)}
