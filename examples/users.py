from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(name=StackOverflow)

# ======== Simple call ========

users = site.get_users([1, 2])

for u in users:
    print(f'User with name {u.display_name} and reputation {u.reputation}')

# ======== Getting answers ========

user = site.get_user(1)

answers = user.get_answers()

print(f'Answers by user {user.display_name}:')
for a in answers:
    print(f'\tAnswer with ID {a.answer_id} and score {a.score}')

# ======== Getting badges ========

user = site.get_user(1)

badges = user.get_badges(pagesize=100)  # Big value of `pagesize` to get all badges.

print(f'Badges, that user {user.display_name} has:')
for b in badges:
    print(f'\t{b.rank} badge "{b.name}"')
