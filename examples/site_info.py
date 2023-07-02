from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

res = site.get_info()

info = res['items'][0]

print(f'Total questions on SO: {info.total_questions}')
