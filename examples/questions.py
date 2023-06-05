from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(name=StackOverflow)

res = site.get_questions([4, 6])

for q in res:
    print(f'Question with title "{q.title}" and score {q.score} by {q.owner["display_name"]}.')
