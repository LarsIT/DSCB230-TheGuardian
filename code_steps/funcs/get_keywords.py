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

# review tomorrow, probably can reuse most of the get_keywords function or add the per_day into a flag or sth.
def get_keywords_per_day(dir_path):
    '''
    #### creates a dict with keywords on a date
    in form: {date1: [keyword1, keyword2, ..., keywordN], date2: [...], ..., dateN:[...]}
    '''
    # get list of directory files
    directory = os.listdir(dir_path)
    keyword_per_day = {}

    for file in directory:

        with open(dir_path + '/' + file) as file:
            data = json.load(file)

        results = data['response']['results']
        date = results['webPublicationDate']

        for index,item in enumerate(results):
            
            temp: list = []
            working_data = results[index]
            tags = working_data['tags']
            

            for tag in tags:
                if tag['type'] == 'keyword':
                    temp.append(tag['webTitle'])
                
            






