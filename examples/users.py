from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(name=StackOverflow)

# ======= Simple call ========
res = site.get_users([1, 2])

print(res[0].display_name)

# ======= Call with parameters ========
res = site.get_users([1, 2, 3, 4], sort='reputation')

for user in res:
    print(f'{user.account_id}: {user.display_name}')
