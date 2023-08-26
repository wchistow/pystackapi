# PyStackAPI developers' guide

## [Development iteration](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#development-iteration)

1. write tests (see [tests' structure](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#tests-structure));
2. implement necessary feature in the library;
3. run MyPy, PyLint and test (see about [running MyPy, PyLint and tests](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#running-mypy-and-tests));
4. commit changes;
5. push commit.

---

## [Tests' structure](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#tests-structure)

For example, you are implementing the `get_comment` method.

1. add file `test_get_answer.py` to directory `tests/test_client`;
2. at the beginning of it there should be this code:
   ```python
   """Tests for `Site.get_answers` and `Site.get_answer`."""
   import lest
   
   from pystackapi import site as site_m
   from pystackapi.item import Item
   
   from . import API_VERSION, requests
   
   site_m.__dict__['requests'] = requests
   site = site_m.Site('stackoverflow')
   
   
   @lest.setup
   def reset_requests() -> None:
       requests.reset()
   ```
3. then, there should be the following methods:
    + `test_get_answers_without_ids_url` - tests that method `get_answers` without transmitting identifiers to it applies to the desired URL;
    + `test_get_answers_with_ids_url` - tests that method `get_answers` with transmitting some identifiers to it applies to the desired URL;
    + `test_get_answers_return_value` - tests that method `get_answers` returns desired list of class `Item`'s instances (desired is `[Item({'id': 1})]`);
    + `test_get_answer_url` - tests that method `get_answer` applies to the desired URL;
    + `test_get_answer_return_value` - tests that method `get_answer` returns desired instance of class `Item` (desired is `Item({'id': 1})`);
    + `test_get_answer_with_no_data` - tests that method `get_answer` returns `None` when the `'items'` key of response is empty list.

For more details, see file [`tests/test_client/test_get_answers.py`](https://github.com/wchistow/pystackapi/blob/master/tests/test_client/test_get_answers.py).

---

## [Running MyPy, PyLint and tests](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#running-mypy-and-tests)

1. In first, install requirements of library from file `requirements.txt`:
   ```shell
   pystackapi$ pip install -r ./requirements.txt
   ``` 
2. Then, install all developer's requirements:
   ```shell
   pystackapi$ pip install -r ./dev_requirements.txt
   ```
3. Run MyPy:
   ```shell
   pystackapi$ python -m mypy ./src/
   ```
4. Run PyLint:
   ```shell
   pystackapi$ python -m pylint ./src/
   ```
5. Run tests:
   ```shell
   pystackapi$ cd tests
   pystackapi/tests$ python main.py
   ```

> Note: if you already installed all requirements, you can run MyPy, PyLint and tests by command
> ```shell
> pystackapi$ python -m mypy ./src/; python -m pylint ./src/; cd tests; python main.py
> ```

---
