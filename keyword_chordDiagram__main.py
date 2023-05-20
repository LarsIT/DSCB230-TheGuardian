import code_steps.funcs.get_keywords as kw
import code_steps.analysis.article_per_day as analysis
import plotly.express as px
from plotapi import Chord

import os
import json

import pandas as pd

def create_co_occurrence_matrix(articles:list):
    '''
    #### Creates a Co-Occurrence Matrix for Keywords

    Important Note:
        The relationships between the Keywords are bidirectional

    ---
    Args:
        articles (list) : a list of lists, where each sublist contain all keywords of an individual article
    ---
    Returns: A Co-Occurrence
    
    '''
    # Create a sorted list of distinct keywords
    keywords = sorted(list(set(keyword for article in articles for keyword in article)))
    
    # Create an empty DataFrame to store the co-occurrence counts
    co_occurrence_matrix = pd.DataFrame(0, index=keywords, columns=keywords)
    
    # Iterate over each article
    for article in articles:

        # Iterate over each keyword in the article
        # Since Relationships are bidirectional we have to iterate over each article multiple times
        # That way we assure that we update the Co-Occurrences from every Keyword's "Perspective"
        for keyword_1 in article:
            # Iterate over the remaining keywords in the article
            for keyword_2 in article:
                # Skip if both keywords are the same
                # This creates zeros on the main diagonal
                if keyword_1 == keyword_2:
                    continue
                
                # Increment the co-occurrence count of the keywords
                co_occurrence_matrix.loc[keyword_1, keyword_2] += 1
    
    return co_occurrence_matrix


if __name__ == '__main__':
    
    path: str = 'data/gcp'
    # create list of distinct keywords
    keywords_complete: list = []


    keywords_complete = kw.get_keywords(path)

    matrix = create_co_occurrence_matrix(keywords_complete).values
    transformed_matrix: list = []
    transformed_row: list = []

    # create new matrix to change Dtypes of all sublists and items of sublists
    for row in matrix:
        for item in row:
            transformed_row.append(int(item))
        transformed_matrix.append(list(transformed_row))

    keywords = sorted(list(set(keyword for article in keywords_complete for keyword in article)))

    # write matrix to different file, because cpu go brrrrrrr
    with open('chord_matrix.py', 'w') as file:
        file.write(f'matrix = {transformed_matrix}')

    #Chord(transformed_matrix, keywords).show()
        



