import requests, os, json

import requests, os, json
BASE_URL = "https://api.football-data.org/v2/"
TOKEN = "8cf37b6a730a44c9874ec696b49dd933"
header = {'Authorization': f'Bearer {TOKEN}'}
path_base = os.path.dirname(os.path.abspath(__file__))
def getCompetitions():
    r = requests.get(f'{BASE_URL}competitions',headers=header)
    print(r.json())
    print(r.status_code)
    with open(f'{path_base}/userPosts.json', 'w',  encoding='UTF-8') as archivo:
            archivo.write(json.dumps(r.json(), indent=4))
    for competicion in r.json()['competitions']:
        print(competicion['name'])
getCompetitions()