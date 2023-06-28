# make heatmap mapping all authors across all dates the dataset includes
# increase the pixel in color-value when the author uploaded an article on that date
import json
from datetime import datetime as dt
import os
import pandas as pd
from keyword_chordDiagram__main import transform_co_occurrence
import plotly.express as px

authors: list = []
timestamps: list = []
author_date_publish :list = []

for file in os.listdir('data'):

    with open(f'data\{file}') as infile:
            data = json.load(infile)

    articles = data['response']['results']

    # set up the matrix
    for item in articles:
        # get date
        date = item['webPublicationDate'][:10]
        timestamps.append(date)

        # get authors
        for tag in item['tags']:
            if tag['type'] == 'contributor':
                    
                    authors.append(tag['webTitle'])
        
                    author_date_publish.append((tag['webTitle'], date))
        


# remove redundances in authors and timestamps
timestamps = list(set(timestamps))
# change list in order to search for dependencies between Authors
authors = sorted(['Paul Karp', 'Martin Pengelly', 'Editorial', 'Peter Walker', 'Guardian Sport', 'Peter Hannam', 'Guardian community team', 'Martin Belam', 'Aubrey Allegretti', 'Alex Lawson'])
author_date_publish_reduced = []

for i in author_date_publish:
    if i[0] in authors:
         author_date_publish_reduced.append(i)
     

# order timestamps
timestamps = [dt.strptime(ts, "%Y-%m-%d") for ts in timestamps]
timestamps.sort()
timestamps = [dt.strftime(ts, "%Y-%m-%d") for ts in timestamps]

# create matrix
matrix = pd.DataFrame(0, index=authors, columns=timestamps)

for entry in author_date_publish_reduced:
    matrix.loc[entry[0], entry[1]] += 1

#matrix = transform_co_occurrence(matrix.values)

# Replace values not equal to 0 with 1
matrix = matrix.applymap(lambda x: 1 if x != 0 else x)

color_scale = [
    [0, 'rgb(255,255,255)'], # white
    [1, 'rgb(0, 0, 255)'] # blue
]



fig = px.imshow(
    matrix,
    x=timestamps,
    y=authors,
    title= 'Days where Authors published',
    color_continuous_scale=color_scale,
    aspect='equal'
    )

# show all authors on y axis
fig.update_layout(
     yaxis_nticks=len(authors)
)

fig.layout.height = 1000
fig.layout.width = 1000
fig.write_html(
     'plots_and_diagrams/Days where TOP10 authors published.html'
)
        


