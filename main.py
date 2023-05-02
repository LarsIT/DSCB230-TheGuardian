import code_steps.funcs.get_keywords as kw
import os
import json

if __name__ == '__main__':
    """
    # get all keywords of test data set and order them

    keywords = kw.get_keywords('data/testdatensatz')

    count: dict = {}

    for article in keywords:
        for tag in article: 
            count[tag] = 1 if tag not in count else count[tag] + 1 
    
    #sort count based on value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True)) 
    
    #remove all keywords with count less than 3

    count = {key: val for key, val in count.items() if val > 50}

    print(count)
    """
    count = 0
    # keyword count per unique day
    for item in os.listdir('data/gcp'):
        with open(f'data/gcp/{item}') as file:
            data = json.load(file)
        
        for article in data['response']['results']:
            count += 1
        
    print(count)
        
            

