import requests
import json


response= requests.get('https://randomuser.me/api?results=10')
data=response.json()

for names in data['results']:
    if names['gender']=="female":
        print("\n")
        print(f"The First Name is {names['name']['first']} and the last name is {names['name']['last']}")


if 1:
    print("\nTruthiness")

if 0:
    print("\n Falsiness")





