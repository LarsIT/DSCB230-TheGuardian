import json
#

#deserializing data and storing it in variable as dictionary
with open('data/data1.json','r') as jsonfile:
    response = json.load(jsonfile) #for some reason it has to be loaded twice in order to get a dictionary

#filtering out useful information
response = response['response']['results']


#get number of articles contained i response

article_num = -1

for i in  range(2): #replace range(2) with response variable
    article_num += 1

    #headline of article
    headline_raw = response[article_num]['fields']['headline']

    #body of article
    body_raw = response[article_num]['fields']['bodyText']

    #creating a unique filename
    j = 0
    article_tags = response[article_num]['tags'] #index after results is the article index in response
    contributor_list = []

    #finding sectionId == Environment for starters
    section_id = response[article_num]['sectionId']

    #finding publication date
    publication_date = response[article_num]['webPublicationDate'][0:10]

    #finding contributors and adding to list
    for i in article_tags:
        if article_tags[j].get('type') == 'contributor':
            contributor_list.append(article_tags[j].get('webTitle'))
        j += 1

    #sort list
    contributor_list.sort()

    #unique filename
    filename = f'{section_id}_{publication_date}_{contributor_list}'

    with open(f'text/{filename}.txt','w') as data:
        data.write(f'{headline_raw}\n{body_raw}')

    print(contributor_list)
