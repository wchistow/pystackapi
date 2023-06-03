import json

from pystackapi import Client
from pystackapi.sites import StackOverflow

client = Client(site=StackOverflow)

res = client.get_info()

print(res)
print(res.response_info)

for item in res:
    for k, v in item:
        print(f'{k}: {v}')

print(res[0].total_questions)

print(json.dumps(dict(res[0]), indent=4))
