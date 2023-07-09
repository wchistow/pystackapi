from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

info = site.get_info()

print(f'Total questions on SO: {info.total_questions}')
