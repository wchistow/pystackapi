from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(name=StackOverflow)

# ======== Simple call ========

users = site.get_users([1, 2])

for u in users:
    print(f'User with name {u.display_name} and reputation {u.reputation}')

# ========  Getting answers for some user ========

users = site.get_users([1, 2])

answers = users[0].get_answers()

print(f'Answers by user {users[0].display_name}:')
for a in answers:
    print(f'\tAnswer with ID {a.answer_id} and score {a.score}')
print(f'\nTotal: {len(answers)}')
