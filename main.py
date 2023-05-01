import code_steps.funcs.get_keywords as kw
import code_steps.analysis.article_per_day as article_count
import plotly.express as px


if __name__ == '__main__':

    # get all keywords of test data set and order them

    path = 'data/testdatensatz'
    keywords = kw.get_keywords(path)

    count: dict = {}

    # count keywords
    for article in keywords:
        for tag in article: 
            count[tag] = 1 if tag not in count else count[tag] + 1 
    
    # sort count based on value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True)) 
    
    # remove all keywords with count less than 50
    count = {key: val for key, val in count.items() if val > 50}

    #make 2 lists, one with keywords, one with count values
    keywords = [x for x in count]
    frequency = [y for x,y in count.items()]

    # bar plot for keyword frequency across test data set
    fig = px.bar(y= frequency, x= keywords)
    fig.show()

    # avg article per day
    print(f'Durchschnittliche Anzahl von Artikeln pro Tag: {article_count.avg_article_per_day(path)}')


    # keywords pro tag
    # dict in form {date1: [keyword1, keyword2, ..., keywordN], date2: [...], ..., dateN:[...]}

    