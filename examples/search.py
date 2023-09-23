from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

# Search for questions about Python
about = site.search(intitle = 'Python')
q1 = about[0]

# Search for the topic Python
topic = site.search(tagged = 'Python')
q2 = topic[0]

# Either `intitle` or `tagged` should be passed
# otherwise BadArgumentsError is passed
print(f'{q1}\n')
print(f'{q2}\n')
