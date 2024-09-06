from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

comments = site.get_comments_on_questions([11])

for comment in comments:
    print(comment.score)  # Priting the number of votes
