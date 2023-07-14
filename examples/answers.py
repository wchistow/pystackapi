from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

answers = site.get_answers([7, 12])

answer = site.get_answer(18)

print(answers)
print(answer)
