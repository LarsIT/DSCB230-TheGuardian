import json

# what this does
# query in the json for specified keys
# display the title of articles that meet a certain value of said specified key
# for example: all article titles that are legally sensitive 

def find_key_path(key: str, json_obj: str, path: str=''):
    '''
    #### searches through a json_object for a specific key and returns the fastest path to the searched key

    ---
    params:
        key (str) : key to search in json object

        json_object (str) : json or dict to be searched in
    
    ---
    returns:
        result (str) : path string, similar to a filepath, with the values seperated by '/'

        returns None if nothing is found
    '''

    if isinstance(json_obj, dict):
        for k, v in json_obj.items():

            # if key found return path to it
            if k == key:
                return path + '/' + k
            
            # in case of value being a dict
            # enter it and search through it for key or more nested dicts or lists
            elif isinstance(v, (dict, list)):
                result = find_key_path(key, v, path + '/' + k) # v is our new json object, 
                if result:
                    return result
                
    # in case of json_obj being a list
    # go through all items to check for key and more nested dicts or lists
    elif isinstance(json_obj, list):
        for i, item in enumerate(json_obj):
            result = find_key_path(key, item, path + '/' + str(i))
            if result:
                return result
    return None

with open('data/gcp/20230330_page1_65e874c2-564a-45be-930c-d0c84f4b3734.json') as json_data:

    # Parse the JSON data
    data = json.load(json_data)

articles = data['response']['results']

interesting_keys = [
    #'isInappropriateForSponsorship',
    'legallySensitive'
    #'shouldHideAdverts',
    #'shouldHideReaderRevenue'
]

# init key count
key_count: dict = {k:0 for k in interesting_keys}
paths: list = []

# get paths to interesting_keys in our json
for object in articles:
    # query for interesting_keys in articles and count occurrences of them
    for i_key in interesting_keys:
        key_found = find_key_path(i_key, object)
        if key_found:
            paths.append(key_found)
            key_found = None

paths = list(set(paths))
print(paths)


for article in articles:
    current_object = article

    keys = paths[0].split('/')[1:]
    for key in keys:
        current_object = current_object[key]
    
    if current_object == 'true':
        print(article['webTitle'])




    