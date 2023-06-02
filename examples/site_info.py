import json

from pystackapi import Client
from pystackapi.sites import StackOverflow

client = Client(site=StackOverflow)

res = client.call('info/')

print(res)

for k, v in res:
    print(f'{k}: {v}')

print(res.total_questions)

print(json.dumps(dict(res), indent=4))

print(res.response_info)
