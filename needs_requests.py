import requests

r = requests.get('https://api.chucknorris.io/jokes/random')
print(r.json()['value'])
