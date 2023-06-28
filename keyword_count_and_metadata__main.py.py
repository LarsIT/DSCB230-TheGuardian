import code_steps.funcs.get_keywords as kw
import code_steps.analysis.article_per_day as analysis
import plotly.express as px


import os
import json



if __name__ == '__main__':
    
    
    # get all keywords of test data set and order them
    path = 'data'
    keywords = kw.get_keywords(path)

    # avg article per day
    print(f'Average number of articles published per day: {analysis.avg_article_per_day(path)}')

    article_count: int = 0
        
    # how many articles are we looking at?
    for item in os.listdir(path):
        with open(f'data/{item}') as file:
            data = json.load(file)
        
        for article in data['response']['results']:
            article_count += 1
        
    print(f'We are currently looking at {article_count} articles.')


    keyword_count: dict = {}
    
    # count occurences of keywords
    for article in keywords: # an article here is a list of keywords of an article
        for tag in article: 
            keyword_count[tag] = 1 if tag not in keyword_count else keyword_count[tag] + 1 

            
    
    # sort count of keywords based on value(frequency)
    keyword_count = dict(sorted(keyword_count.items(), key= lambda y: y[1],reverse=True)) 
    
    # remove all keywords with count less than 200
    keyword_count = {key: val for key, val in keyword_count.items() if val > 200}


    # prepare keyword count for plot
    # make 2 lists, one with keywords, one with count values
    
    keywords = [x for x in keyword_count]
    frequency = [y for x,y in keyword_count.items()]

    # bar plot for keyword frequency across 
    fig = px.bar(y= frequency, x= keywords, title= 'Occurences of Keywords')
    fig.write_html('plots_and_diagrams/General Occurrences of Keywords.html')

    # pie plot showing the same data
    fig = px.pie(values=frequency, names=keywords, title= 'Relative Frequency of Keywords')
    fig.write_html('plots_and_diagrams/General Relative Frequency of Keywords.html')

    
