import json


with open('data/20230323_page1.json') as file:
    data = json.load(file)

results = data['response']['results']
keywords_complete: list = []

for i in range(len(results)):
    
    working_data = data['response']['results'][i]
    tags = working_data['tags']
    temp: list = []

    for j in tags:
        if j['type'] == 'keyword':
            temp.append(j['webTitle'])
    
    keywords_complete.append(temp)
    print(temp)





