"""Tests for class `Site`."""
from mocks import RequestsMock

# instance of class `RequestsMock` is defined here,
# because functions `reset_requests` in all modules `./test_*.py`
# have to referenced to the same object.
requests = RequestsMock(return_items=[{'id': 1}])

API_VERSION = '2.3'

from . import test_get
from . import test_get_answers
from . import test_get_articles
from . import test_get_badges
from . import test_get_collectives
from . import test_get_comments
from . import test_get_favorites
from . import test_get_info
from . import test_get_linked
from . import test_get_mentiones
from . import test_get_posts
from . import test_get_privileges
from . import test_search
from . import test_get_suggested_edits
from . import test_get_questions
from . import test_get_related
from . import test_get_revisions
from . import test_get_tags
from . import test_get_timeline
from . import test_get_users
