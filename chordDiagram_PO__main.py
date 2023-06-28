import code_steps.funcs.get_keywords as kw
from plotapi import Chord
import pandas as pd
import json
import keyword_chordDiagram__main as CDiagram
import os

def count_items(arr=[]) -> dict:
    '''counts items of datastructure and returns a sorted dictionary'''
    count: dict = {}

    # count items in array
    for item in arr:
        count[item] = 1 if item not in count else count[item] + 1

    # sort count by value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True))

    return count


def create_chordDiagram(data_path: str = 'data',
                        save_location: str = 'plots_and_diagrams', 
                        location: str = 'all', 
                        top_number_keywords: int = 15
                        ) -> None:
    '''
    #### creates a Chord Diagram and saves it to an html-file

    ---
    params: 
        - data_path (str) : filepath to data directory
        
        - save_location (str) : filepath to directory where chord diagram is saved

        - location (str) : filters articles based on production office \n
            Options: \n
                all : standard value for location, doesn't filter articles, it takes all \n
                UK : for UK production office \n
                US : for US production office \n
                AUS : for AUS production office \n
                

        - top_number_keywords (int) : Chord Diagram is limited to a maximum of 15 NODES/ARCS \n
                                    setting this value moves this 15 ARCS sized interval around, \n
                                    this parameter represents the high end of the inverval \n

    ---
    returns:
        this function doesn't have a return value \n
        it saves a chord diagram in the ```save location``` set above
    '''

    
    # create lists with article objects
    # 3 different lists depending on production office 
    articles: list = []
    keywords: list = []
    keyword_count: dict = {}
    article_count: int = 0
    distinct_keywords: list
        
    
    for item in os.listdir(data_path):
        with open(f'data\{item}') as file:
            data = json.load(file)

        articles_of_current_file: list = data['response']['results']



        for article in articles_of_current_file:

            tags = article['tags']

            # group all articles based on location of publishment
            # increment location based article count
            # extract keywords of articles and group them based on location

            # if location is set filter articles based on location, 
            if article['fields']['productionOffice'] == location or location == 'all':
                articles.append(article)

                article_count += 1
                temp: str = ''

                for tag in tags:
                    
                    keyword_title = tag['webTitle']

                    # since an article can have the same keyword multiple times the count may become inflated
                    # we use temp to save the last keyword tag in order to avoid adding the same keywords multiple times
                    if tag['type'] == 'keyword':
                        keywords.append(keyword_title)
                        
            else:
                continue

    # create keyword count 
    keyword_count = count_items(keywords)
    # sort count of keywords based on value(frequency)
    keyword_count = dict(sorted(keyword_count.items(), key= lambda y: y[1],reverse=True)) 
    # get top 15 keywords, more than 15 keywords at a time make the diagram too cluttered
    keyword_limit = 15 
    
    keyword_count = {key: keyword_count[key] for key in list(keyword_count)[top_number_keywords-keyword_limit:top_number_keywords]}
    
    # get distinct keywords for chord diagram
    distinct_keywords = sorted(list(set(keyword for keyword in keyword_count)))  

    # create the article lists containing only keywords
    only_keywords_from_articles = kw.get_keywords_in_loop(articles)

    # create Co-Occurrence Matrix
    matrix = CDiagram.create_co_occurrence_matrix(only_keywords_from_articles, keyword_count).values
    matrix = CDiagram.transform_co_occurrence(matrix)
    
    #Create Chord Diagram
    diagram =  Chord(    
        matrix= matrix,
        names= distinct_keywords,
        arc_numbers= True, 
        width= 800
        )
    
    diagram.to_html(filename= f'{save_location}/{location}_TOP({top_number_keywords-keyword_limit} to {top_number_keywords})_chordDiagram.html')


if __name__ == '__main__':
    #create_chordDiagram(location='AUS')  
    create_chordDiagram(location='UK') 
    create_chordDiagram(location='US')
    create_chordDiagram()
