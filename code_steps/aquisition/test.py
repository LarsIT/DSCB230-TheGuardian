import json

with open('data/data gcp/20230330_page1_65e874c2-564a-45be-930c-d0c84f4b3734.txt','r') as file:
    x = file.read()
    x = json.loads(x)

for i in x['response']:
    print(i)