import code_steps.funcs.get_keywords as kw
import pandas as pd
import plotly.express as px


if __name__ == '__main__':

    # get all keywords of test data set and order them

    keywords = kw.get_keywords('data/testdatensatz')

    count: dict = {}

    #count keywords
    for article in keywords:
        for tag in article: 
            count[tag] = 1 if tag not in count else count[tag] + 1 
    
    #sort count based on value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True)) 
    
    #remove all keywords with count less than 50
    count = {key: val for key, val in count.items() if val > 50}

    #make 2 lists, one with keywords, one with count values
    keywords = [x for x in count]
    frequency = [y for x,y in count.items()]

    #bar plot
    fig = px.bar(y= frequency, x= keywords)
    fig.show


