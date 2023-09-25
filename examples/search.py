from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

# Search for questions with word "Python" in title
about = site.search(intitle='Python')
q1 = about[0]  # First returned question

# Search for questions with tag [python]
topic = site.search(tagged='python')
q2 = topic[0]

# Either `intitle` or `tagged` should be passed
# otherwise `BadArgumentsError` is passed
print(f'{q1}\n')
print(f'{q2}\n')
