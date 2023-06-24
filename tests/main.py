import lest

import sys

sys.path.insert(0, '../src')

import test_models.test_answer
import test_models.test_base
import test_models.test_question
import test_models.test_user

import test_response
import test_item

if __name__ == '__main__':
    lest.run()
