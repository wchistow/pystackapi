from pystackapi import Site
from pystackapi.sites import StackOverflow

client = Site(name=StackOverflow)

# ======= Simple call ========
res = client.get_users([1, 2])

print(res[0].display_name)

# ======= Call with parameters ========
res = client.get_users([1, 2], sort='reputation', order='asc')

print(res[0].display_name)
