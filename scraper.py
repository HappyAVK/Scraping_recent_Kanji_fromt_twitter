import os
import snscrape
import pandas as pd
import regex as re


def Get_Japanese_Tweets():
    kanji_list = []
    os.system("snscrape --jsonl --max-results 100 twitter-search \"lang:ja\"> JP-tweets.json")
    df = pd.read_json('JP-tweets.json', lines=True)

    pattern = re.compile(r'([\p{IsHan}\p{IsBopo}])', re.UNICODE)

    for i, rows in df.iterrows():
        tweet = df.iloc[i,30]
        tweet = tweet.replace("("," ")
        new_tweet = pattern.sub(r'(\1)', tweet)

        kanji = re.findall(r'\((.*?)\)', new_tweet)

        kanji_list.extend(kanji)

    kanji_frequency_data = {}
    for kanji in kanji_list:
        kanji_frequency_data[kanji] =kanji_list.count(kanji)

    return kanji_frequency_data

if __name__ == "__main__":
    Get_Japanese_Tweets()