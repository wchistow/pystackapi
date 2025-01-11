import lest

import sys

sys.path.insert(0, '../src')

from mocks import RequestsMock, ChatexchangeClientMock

# instance of class `RequestsMock` is defined here,
# because functions `reset_requests` in all modules `./test_*.py`
# have to referenced to the same object.
requests = RequestsMock(return_items=[{'id': 1}])
chatexchange = ChatexchangeClientMock(email='user@example.com', password='testpass')

API_VERSION = '2.3'

import test_base_client
import test_chat
import test_network
import test_site
import test_item

if __name__ == '__main__':
    lest.run()
