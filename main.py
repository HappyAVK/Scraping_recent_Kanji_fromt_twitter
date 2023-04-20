import snscrape
import streamlit as st
import os

os.system("snscrape --jsonl --max-results 100 twitter-search \"lang:ja\"> user-tweets.json")


