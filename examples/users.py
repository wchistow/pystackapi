from pystackapi import Site
from pystackapi.sites import StackOverflow

client = Site(name=StackOverflow)

res = client.get_users([1, 2])

print(res[0].display_name)
