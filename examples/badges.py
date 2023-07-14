from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

badges_recipients = site.get_badges_recipients([1, 2, 3])

tag_based_badges = site.get_tag_based_badges(pagesize=5)

print(badges_recipients)
print(tag_based_badges)
