import json

keywords_complete: list = []

for k in range(1,3):

    with open(f'data/20230323_page{k}.json') as file:
        data = json.load(file)

    results = data['response']['results']

    for i in range(len(results)):
        
        working_data = data['response']['results'][i]
        tags = working_data['tags']
        temp: list = []

        for j in tags:
            if j['type'] == 'keyword':
                temp.append(j['webTitle'])
        
        keywords_complete.append(temp)
        print(temp)





