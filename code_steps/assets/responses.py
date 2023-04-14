import json


class Response:

    def __init__(self):
        pass
        
    def get_status(filename:str):
        with open(f'/media/lars/Elements/theguardian.com/text_processor/data/{filename}.json','r') as jsonfile:
            response = json.load(jsonfile)

        response = response['response']

        print(f'''
        Status...{response['status']}
        Permission...{response['userTier']}
        Number of results...{response['total']}
        ''')

        return response, response['status']