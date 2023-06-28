import code_steps.funcs.get_keywords as kw
import code_steps.analysis.article_per_day as analysis
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import os
import json
import datetime


if __name__ == '__main__':    


    #plot the article count per day and average word count per day, side by side

    # path to data directory
    dir_path = 'data'

    keywords_complete: list = []
    directory : list = []

    # get list of all files in data directory
    directory = os.listdir(dir_path)

    article_per_day: dict = {}
    wordcount_per_day_complete: dict = {}
    avg_wordcount_per_day: dict = {}

    i: int = 0 # counter

    for file in directory:

        with open(dir_path + '/' + file) as file:
            data = json.load(file)

        # access list of all articles from api response
        results = data['response']['results']


        # iterate over articles
        for article in results:

            # count articles per day
            date: str = article['webPublicationDate'][:10]

            if date in article_per_day:
                article_per_day[date] += 1
            
            else:
                article_per_day[date] = 1


            # for each individual day, create a list of wordcounts from articles of that day
            if date in wordcount_per_day_complete:             
                wordcount_per_day_complete[date].append(int(article['fields']['wordcount']))

            else:
                wordcount_per_day_complete[date] = [int(article['fields']['wordcount'])]


    # make the average word count for every day
    for date in wordcount_per_day_complete:
        avg_wordcount_per_day[date] = sum(wordcount_per_day_complete[date]) / article_per_day[date]


    # sort avg_wordcount
    avg_wordcount_per_day = sorted(avg_wordcount_per_day.items(), reverse=True)
    
    # sort article per day
    article_per_day = sorted(article_per_day.items(), reverse=True)


    # Create subplot with two subplots, one for each line plot
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    # Plot article per day (blue)
    date = [x[0] for x in article_per_day]
    frequency = [x[1] for x in article_per_day]

    fig.add_trace(go.Scatter(x=date, y=frequency, name='Article per day'), row=1, col=1)

    # Plot average word count per day (red)
    date = [x[0] for x in avg_wordcount_per_day]
    frequency = [x[1] for x in avg_wordcount_per_day]

    fig.add_trace(go.Scatter(x=date, y=frequency, name='Average Word Count per day'), row=2, col=1)

    # Update layout
    title = 'Article per day and Average Word Count per day'
    fig.update_layout(title= title, height=1000)

    # Show figure
    fig.write_html(f'plots_and_diagrams\{title}.html')