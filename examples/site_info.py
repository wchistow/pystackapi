import json

from pystackapi import Client
from pystackapi.sites import StackOverflow

client = Client(site=StackOverflow)

print(json.dumps(client.call('info/'), indent=4))
