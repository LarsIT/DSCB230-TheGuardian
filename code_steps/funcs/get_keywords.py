import json
import os

def get_keywords(dir_path):
    '''
    #### creates list of keywords of an article
    '''

    keywords_complete: list = []
    directory = os.listdir(dir_path)

    # get list of directory files
    for file in directory:

        with open(dir_path + '/' + file) as file:
            data = json.load(file)

        results = data['response']['results']

        for index,item in enumerate(results):
            
            temp: list = []
            working_data = results[index]
            tags = working_data['tags']
            

            for tag in tags:
                if tag['type'] == 'keyword':
                    temp.append(tag['webTitle'])
            
            keywords_complete.append(temp)
        
    return keywords_complete


def get_keywords_in_loop(articles: list):

    keywords_complete: list = []

    for index,item in enumerate(articles):
            
            temp: list = []
            working_data = articles[index]
            tags = working_data['tags']
            

            for tag in tags:
                if tag['type'] == 'keyword':
                    temp.append(tag['webTitle'])
            
            keywords_complete.append(temp)
        
    return keywords_complete



