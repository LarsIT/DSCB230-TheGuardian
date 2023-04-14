import json
import requests
from datetime import date, timedelta
from time import sleep


yesterday = date.today() - timedelta(1)
file_date = str(yesterday).replace('-','')

with open('code steps/api/key.txt','r') as api_key:
    api_key = api_key.read()


response = requests.get(f'https://content.guardianapis.com/search?from-date={yesterday}&page-size=200&api-key={api_key}').json()
max_pages = response['response']['pages']


for page in range(max_pages):
    page += 1 
    sleep(5)
    
    response = requests.get(
        f'https://content.guardianapis.com/search?from-date={yesterday}&page={page}&page-size=200&format=json&show-references=all&show-fields=all&show-tags=all&show-section=true&show-blocks=all&show-elements=all&show-rights=all&api-key={api_key}'
     ).json()

    with open(f'data/{file_date}_page{page}.json','w') as jsonfile:
        json.dump(response, jsonfile)

    





