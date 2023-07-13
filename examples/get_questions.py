from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

questions = site.get_questions([9, 11])

question = site.get_question(4)

print(questions)
print(question)
