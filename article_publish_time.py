import json
import plotly.express as px
import os
from datetime import datetime as dt
import pandas as pd
from plotapi import HeatMap
from keyword_chordDiagram__main import transform_co_occurrence

# make a bar chart for number of articles published across 24 hours
article_hour_count = {}
weekdays: list = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]
timespan = range(0,24)


def convert_to_dayname(date:str) -> str:
    '''
    #### returns the name of the day from a date
    
    ---
    requirements:
        - datetime.datetime as dt (python built-in library)
    ---
    params:
        - date (str) : date string in format YEAR-MONTH-DAY

    ---
    returns:
        Name of the date's day (str)
    '''

    date_format = "%Y-%m-%d"
    day_conversion = {
        '0': 'Monday',
        '1': 'Tuesday',
        '2': 'Wednesday',
        '3': 'Thursday',
        '4': 'Friday',
        '5': 'Saturday',
        '6': 'Sunday'
    }

    date = dt.strptime(date,date_format)

    day = dt.weekday(date)

    return day_conversion[str(day)]

matrix = pd.DataFrame(0, index=weekdays, columns=timespan)

for item in os.listdir('data/gcp'):
        
    with open(f'data/gcp/{item}') as infile:
        data = json.load(infile)

    articles = data['response']['results']


    for article in articles:
        # get publication hour 
        publication_hour = int(article['fields']['firstPublicationDate'][11:13])
        # get punlication date
        publication_date = article['fields']['firstPublicationDate'][0:10]
        # convert date to day name
        publication_day = convert_to_dayname(publication_date)
        
        # update matrix at intersection of day and hour
        matrix.loc[publication_day, publication_hour] += 1

matrix = transform_co_occurrence(matrix.values)

timespan = [str(x) for x in timespan]

px.imshow(
    matrix,
    x=timespan,
    y=weekdays,
    title= 'Publications acrooss Days and Daytime'
    
    ).write_html('plots_and_diagrams/Publications acrooss Days and Daytime.html')


    # break is only for testing



'''
x,y = [x for x,y in article_hour_count.items()], [y for x,y in article_hour_count.items()]
fig = px.bar(x=x, y=y, title='Number of Articles published throughout the day')

# update layout for xaxis tickmode as linear in order to show all x values
fig.update_layout(
   xaxis = dict(
      tickmode = 'linear',
   )
)

fig.show()
'''


