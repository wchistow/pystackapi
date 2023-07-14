from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

users = site.get_users([2, 3])

user = site.get_user(1)

print(users)
print(user)
