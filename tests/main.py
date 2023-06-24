import lest

import sys

sys.path.insert(0, '../src')

from test_models import *

import test_response
import test_item

if __name__ == '__main__':
    lest.run()
