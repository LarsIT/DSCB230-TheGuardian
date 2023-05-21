import code_steps.funcs.get_keywords as kw
from plotapi import Chord
import pandas as pd
import json

def count_items(arr=[]) -> dict:
    '''counts items of datastructure and returns a sorted dictionary'''
    count: dict = {}

    # count items in array
    for item in arr:
        count[item] = 1 if item not in count else count[item] + 1

    # sort count by value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True))

    return count

def create_co_occurrence_matrix(articles: list, threshhold: dict):
    '''
    #### Creates a Co-Occurrence Matrix for Keywords

    Important Note:
        The relationships between the Keywords are bidirectional

    ---
    Args:
        articles (list) : a list of lists, where each sublist contain all keywords of an individual article

        threshhold (dict) : a count dictionary, that counts occurrences of keywords to a specific threshhold

             with threshhold a count threshhold is meant, e.g. it doesn't contain keywords with a count less than 200(or a different value) 
    
    ---

    Returns: A Co-Occurrence
    
    '''
    if not threshhold:
        # create a threshhold for relevant keywords, since RAM go brrrrr
        with open('kw_count.json','r') as infile:
            threshhold = json.load(infile)
        

        # Create a sorted list of distinct keywords
        keywords = sorted(list(set(keyword for article in articles for keyword in article if keyword in threshhold)))
    else:
        keywords = sorted(list(set(keyword for article in articles for keyword in article if keyword in threshhold)))

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
                if keyword_1 in threshhold and keyword_2 in threshhold:
                    co_occurrence_matrix.loc[keyword_1, keyword_2] += 1
    
    return co_occurrence_matrix

def transform_co_occurrence(matrix):
    '''transform dataframe matrix into list of lists'''
    # create new matrix to change Dtypes of all sublists and items of sublists
    transformed_matrix = []

    for row in matrix:
        transformed_row: list = []

        for item in row:
            transformed_row.append(int(item))
            
        transformed_matrix.append(list(transformed_row))
        
    return transformed_matrix
    


if __name__ == '__main__':
    
    path: str = 'data/testdatensatz'
    # create list of distinct keywords
    keywords_complete: list = []


    keywords_complete = kw.get_keywords(path)
    keyword_count = count_items(keywords_complete)
    keyword_count = dict(sorted(keyword_count.items(), key= lambda y: y[1],reverse=True))
    keyword_count = {key: keyword_count[key] for key in list(keyword_count)[:15]}
    distinct_keywords = sorted(list(set(keyword for keyword in keyword_count))) 


    matrix = create_co_occurrence_matrix(keywords_complete, keyword_count).values
    
    transformed_matrix = transform_co_occurrence(matrix)
    
    Chord(matrix= transformed_matrix,  
      names= distinct_keywords,
      arc_numbers= True, 
      colored_diagonals= False, 
      padding= 0.02, 
      width= 1000,
      title= 'Co-Occurrence of Keywords from TheGuardian.com articles of April',
      font_size="12px",
      font_size_large="30px"
      ).to_html(filename= 'test_page1Chord.html')
        



