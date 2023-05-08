import json

with open('data/gcp/20230330_page1_65e874c2-564a-45be-930c-d0c84f4b3734.json') as file:

    data = json.load(file)

results = data['response']['results']

# article count
for index ,item in enumerate(results):
    continue
else:
    print(index+1)


test = {'2':[15]}

test['2'].append(55)
print(test)