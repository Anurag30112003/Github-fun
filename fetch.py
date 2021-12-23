import requests
username = 'Anurag30112003'
#fetchs specific parameter from api request
api = requests.get(f'https://api.github.com/users/{username}')
name = api.json()['login']
url = api.json()['html_url']
repos = api.json()['public_repos']
location = api.json()['location']
print(username,url,repos)