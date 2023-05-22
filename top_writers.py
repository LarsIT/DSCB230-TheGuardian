import os
import json
from plotapi import BarFight
import plotly.express as px

# what is done here
# write an article counter for how many articles the authors worked on
# write a dictionary that shows for how many topics the authors wrote

def count_items(arr=[]) -> dict:
    '''counts items of datastructure and returns a sorted dictionary'''
    count: dict = {}

    # count items in array
    for item in arr:
        count[item] = 1 if item not in count else count[item] + 1

    # sort count by value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True))

    return count

### main program start

writers_keywords: list = []

for item in os.listdir('data/gcp'):
    

    with open(f'data/gcp/{item}') as infile:
        data = json.load(infile)

    articles = data['response']['results']

    for article in articles:
        tags = article['tags']
        

        for tag in tags:
            if tag['type'] == 'keyword':
                keyword = tag['webTitle']

            if tag['type'] == 'contributor':
                writers_keywords.append((tag['webTitle'], keyword))

# make a dictionary that counts articels written by authors
writers = [combination[0] for combination in writers_keywords]
writer_article_count = count_items(writers)
# sorte count by number of articles written
writer_article_count = list(sorted(writer_article_count.items(), key= lambda y: y[1],reverse=True))

# make a dictonary with key being a writer and value being a list of keywords that writer wrote
writer_wrote_topics: dict = {}

for combination in writers_keywords:
    writer = combination[0]
    topic = combination[1]

    if writer not in writer_wrote_topics:
        writer_wrote_topics[writer] = [topic]
    else:
        writer_wrote_topics[writer].append(topic)

# sort writer wrote topics based on how many topics he wrote for
writer_wrote_topics = dict(sorted(writer_wrote_topics.items(), key= lambda y: len(y[1]),reverse=True))

#print(writer_wrote_topics)
# get top 10 authors based on articles written
#print(dict(writer_article_count[:10]))
# make barplot and save it to html

top_10_writers = dict(writer_article_count[:10])
x,y = [x for x,y in top_10_writers.items()], [y for x,y in top_10_writers.items()]
plot_title = 'The Top 10 Authors based on number of articles written'
fig = px.bar(x=x, y=y, title= plot_title)

fig.write_html(f'plots_and_diagrams/{plot_title}.html')