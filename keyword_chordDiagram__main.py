import code_steps.funcs.get_keywords as kw
import code_steps.analysis.article_per_day as analysis
import plotly.express as px
from plotapi import Chord

import os
import json

# What TODO:
# need list of all distinct keywords, ordered alphabetically
# need a matrix with each row representing a distinct keyword in same order as list of distinct keywords
# each column is also a distinct keyword, column order is the same as order of distinct keywords list
# 
# example Matrix 6x6 -> 6 distinct Keywords
# [[0, 5, 6, 4, 7, 4],
#  [5, 0, 5, 4, 6, 5],
#  [6, 5, 0, 4, 5, 5],
#  [4, 4, 4, 0, 5, 5],
#  [7, 6, 5, 5, 0, 4],
#  [4, 5, 5, 5, 4, 0]] 

if __name__ == '__main__':
    
    # create list of distinct keywords

    # load data
    for item in os.listdir('data/gcp'):
        with open(f'data/gcp/{item}') as file:
            data = json.load(file)

        articles: list = data['response']['results']

        #get all keywords
        keywords_complete: list = kw.get_keywords_in_loop(articles)



