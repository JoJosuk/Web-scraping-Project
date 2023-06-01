import requests
import json

api_url ="http://127.0.0.1:5000/"

response=requests.get(api_url)
print(response.json())
exit()
qlist=response.json()
print(len(qlist))
for i in qlist:
    for key in i:
        print(f'{key}:{i[key]}')
    print()