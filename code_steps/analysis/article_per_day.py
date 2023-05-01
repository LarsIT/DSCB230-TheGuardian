import json
import os


def avg_article_per_day(dir_path):
    '''
    #### creates list of keywords of an article
    '''
    day = set()
    count = 0
    keywords_complete: list = []
    directory = os.listdir(dir_path)

    for file in directory:

        # get number of articles across article set
        with open(dir_path + '/' + file) as file:
            data = json.load(file)

        results = data['response']['results']

        for index, item in enumerate(results):
            continue
        else:
            temp_count = index + 1
        
        count += temp_count

        # get number days (timespan)
        for i in results:
            day.add(i['webPublicationDate'][:10])

    return count / len(day)
        
