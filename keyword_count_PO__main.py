import code_steps.funcs.get_keywords as kw
import code_steps.analysis.article_per_day as analysis
import plotly.express as px


import os
import json

# functions
save_location = 'plots_and_diagrams/'

def count_items(arr=[]) -> dict:
    '''counts items of datastructure and returns a sorted dictionary'''
    count: dict = {}

    # count items in array
    for item in arr:
        count[item] = 1 if item not in count else count[item] + 1

    # sort count by value
    count = dict(sorted(count.items(), key= lambda y: y[1],reverse=True))

    return count

def create_barPlot_from_dict(count:dict, production_office: str = 'unkown origin') -> None:
    '''creates a bar plot from a count dictionary'''
    terms, frequency = [x for x in count], [y for x,y in count.items()]
    title = f'Occurences of Keywords in {production_office}'

    # bar plot
    fig = px.bar(y= frequency, x= terms, title= title)
    fig.write_html(save_location + title + '.html')


def create_piePlot_from_dict(count:dict, production_office: str = 'unkown origin')-> None:
    '''creates a pie plot from a count dictionary'''

    terms, frequency = [x for x in count], [y for x,y in count.items()]
    title = f'Relative Frequency of Keywords in {production_office}'

    # pie plot 
    fig = px.pie(values=frequency, names=terms, title= title)
    fig.write_html(save_location + title + '.html')



# make keyword count grouped by production office of article
if __name__ == '__main__':
    
    
    # get all keywords of test data set and order them
    path: str = 'data'

    uk_keywords: list =  []
    us_keywords: list = []
    aus_keywords: list = []

    uk_count : dict = {}
    us_count: dict = {}
    aus_count: dict = {}

    uk_article_count: int = 0
    us_article_count: int = 0
    aus_article_count: int = 0

    # load data
    for item in os.listdir(path):
        with open(f'{path}\{item}') as file:
            data = json.load(file)

        articles: list = data['response']['results']

        for article in articles:

            production_office: str = article['fields']['productionOffice']

            tags = article['tags']
            

            # match produciton office(PO)
            # get all keywords of articles and add them to a PO-specific list
            match production_office:
                

                case 'UK':
                    # add uk keywords
                    # an article can have the same keyword multiople times????
                    temp: str = ''
                    
                    for tag in tags:
                        temp: str = ''
                        keyword_title = tag['webTitle']

                        # since an article can have the same keyword multiple times the count may become inflated
                        # we use temp to save the last keyword tag in order to avoid adding the same keywords multiple times
                        if tag['type'] == 'keyword' and (temp == False or tag != temp):
                            uk_keywords.append(tag['webTitle'])
                            temp = tag['webTitle']        
                                  
                    
                    # increment article count
                    uk_article_count += 1
                    
                case 'AUS':
                    # add aus keywords
                    temp: str = ''

                    for tag in tags:
                        
                        keyword_title = tag['webTitle']

                        if tag['type'] == 'keyword' and (temp == False or tag != temp):
                            aus_keywords.append(tag['webTitle'])
                            temp = tag['webTitle']
                            
                                
                    # increment article count
                    aus_article_count += 1
                    
                case 'US':
                    # add us keywords
                    temp: str = ''

                    for tag in tags:

                        keyword_title = tag['webTitle']

                        if tag['type'] == 'keyword' and (temp == False or tag != temp):
                            us_keywords.append(tag['webTitle'])
                            temp = tag['webTitle']

                    # increment article count
                    us_article_count += 1
                    
                case _:
                    pass


    # create keyword counts
    # create plots
    
    # UK
    uk_count = count_items(uk_keywords)
    # remove all keywords with count less than 
    uk_count = {key: val for key, val in uk_count.items() if val > int(uk_article_count*0.02)}

    create_barPlot_from_dict(uk_count, 'UK')
    create_piePlot_from_dict(uk_count, 'UK')
    
    # US
    us_count = count_items(us_keywords)
    # remove all keywords with count less than 200
    us_count = {key: val for key, val in us_count.items() if val > int(us_article_count*0.02)}

    create_barPlot_from_dict(us_count, 'US')
    create_piePlot_from_dict(us_count, 'US')
      

    # AUS
    aus_count = count_items(aus_keywords)
    # remove all keywords with count less than 200
    aus_count = {key: val for key, val in aus_count.items() if val > int(aus_article_count*0.02)}

    create_barPlot_from_dict(aus_count, 'AUS')
    create_piePlot_from_dict(aus_count, 'AUS')



# make a pie plot showing the distribution of articles on the produciton offices
title = 'Distribution of Articles across Production Offices'
fig = px.pie(values= [uk_article_count, us_article_count, aus_article_count], names= ['UK', 'US', 'AUS'], title= title)
fig.write_html(save_location + title + '.html')


