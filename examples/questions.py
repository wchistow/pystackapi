from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(name=StackOverflow)

# ======== Simple call ========
questions = site.get_questions([4, 6])

for q in questions:
    print(f'Question with title "{q.title}" and score {q.score} by {q.owner["display_name"]}.')

# ======== Getting answers of question ========
questions = site.get_questions([4])
answers = questions[0].get_answers()

print('Answers for question with ID 4:')
for a in answers:
    print(f'\tAnswer by {a.owner["display_name"]} with score {a.score}')

# ======== Getting comments of question ========
questions = site.get_questions([4])
comments = questions[0].get_comments()

print('Comments on question with ID 4:')
for c in comments:
    print(f'\tComment by {c.owner["display_name"]} with score {c.score}')
