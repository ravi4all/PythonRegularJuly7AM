import urllib.request as url
import json

path = "https://api.covid19india.org/states_daily.json"

response = url.urlopen(path)
data = json.load(response)
states = data['states_daily']
# print(len(states))
# print(len(states)/3)

confirmed = []
for i in range(len(states)):
    if states[i]['status'] == 'Confirmed':
        confirmed.append(states[i])

recovered = []
for i in range(len(states)):
    if states[i]['status'] == 'Recovered':
        recovered.append(states[i])

deceased = []
for i in range(len(states)):
    if states[i]['status'] == 'Deceased':
        deceased.append(states[i])

print(confirmed[-1]['tt'])