import code_steps.funcs.get_keywords as kw
import code_steps.analysis.article_per_day as article_count
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import os
import json
import datetime


if __name__ == '__main__':
    """
    # get all keywords of test data set and order them
    path = 'data/gcp'
    keywords = kw.get_keywords(path)

    count: dict = {}

    # count keywords
    for article in keywords:
        for tag in article: 
            count[tag] = 1 if tag not in count else count[tag] + 1 
    
    # sort count based on value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True)) 
    
    # remove all keywords with count less than 200
    count = {key: val for key, val in count.items() if val > 200}

    #make 2 lists, one with keywords, one with count values
    keywords = [x for x in count]
    frequency = [y for x,y in count.items()]

    # bar plot for keyword frequency across test data set
    fig = px.bar(y= frequency, x= keywords)
    fig.show()

    # avg article per day
    print(f'Durchschnittliche Anzahl von Artikeln pro Tag: {article_count.avg_article_per_day(path)}')


    print(count)

    # keywords per tag
    # dict in form {date1: [keyword1, keyword2, ..., keywordN], date2: [...], ..., dateN:[...]}

    
    count = 0
    
    # how many articles are we looking at?
    for item in os.listdir('data/gcp'):
        with open(f'data/gcp/{item}') as file:
            data = json.load(file)
        
        for article in data['response']['results']:
            count += 1
        
    print('Article Count:',count)
    """


    # article count per day as blue line
    # avg text length per day in contrast as red line 
    # iterate over folder


    dir_path = 'data/gcp'

    keywords_complete: list = []
    directory = os.listdir(dir_path)

    # get list of directory files
    article_per_day = {}
    wordcount_per_day_complete = {}
    avg_wordcount_per_day = {}

    i = 0

    for file in directory:

        with open(dir_path + '/' + file) as file:
            data = json.load(file)

        results = data['response']['results']


        # iterate over articles
        # 
        for article in results:

            # data for line diagram, article per day
            date = article['webPublicationDate'][:10]

            if date in article_per_day:
                article_per_day[date] += 1
            
            else:
                article_per_day[date] = 1


            # data for average wordcount per day
            if date in wordcount_per_day_complete:             
                wordcount_per_day_complete[date].append(int(article['fields']['wordcount']))

            else:
                wordcount_per_day_complete[date] = [int(article['fields']['wordcount'])]



    for date in wordcount_per_day_complete:
        avg_wordcount_per_day[date] = sum(wordcount_per_day_complete[date])/article_per_day[date]


    # sort avg_wordcount
    avg_wordcount_per_day = sorted(avg_wordcount_per_day.items(), reverse=True)
    
    # sort article per day
    article_per_day = sorted(article_per_day.items(), reverse=True)


    # Create subplot with two subplots, one for each line plot
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    # Plot article per day
    date = [x[0] for x in article_per_day]
    frequency = [x[1] for x in article_per_day]

    fig.add_trace(go.Scatter(x=date, y=frequency, name='Article per day'), row=1, col=1)

    # Plot average word count per day
    date = [x[0] for x in avg_wordcount_per_day]
    frequency = [x[1] for x in avg_wordcount_per_day]

    fig.add_trace(go.Scatter(x=date, y=frequency, name='Average Word Count per day'), row=2, col=1)

    # Update layout
    fig.update_layout(title='Article per day and Average Word Count per day', height=1000)

    # Show figure
    fig.show()

            

