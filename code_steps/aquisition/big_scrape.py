import json
import requests

#get api key
with open('code steps/api/key.txt','r') as api_key:
    api_key =api_key.read()

i = 0

try:
        
    for i in range(190):
        i += 1 
        #get api response with as much data as possible
        response = requests.get(f'https://content.guardianapis.com/search?page={i}&page-size=200&format=json&show-references=all&show-fields=all&show-tags=all&show-section=true&show-blocks=all&show-elements=all&show-rights=all&api-key={api_key}').json()

        #dumping response into file
        with open(f'data/page{i}.json','w') as jsonfile:
            json.dump(response, jsonfile)
except:
    print(f'Error bei Page {i}')


