import code_steps.funcs.get_keywords as kw
import pandas

if __name__ == '__main__':

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
