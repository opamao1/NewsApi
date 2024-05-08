import json


def get_news():


    with open('Data/data.json') as f:
        data = json.load(f)

        return data
    
    



