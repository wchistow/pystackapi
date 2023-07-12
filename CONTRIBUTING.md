# PyStackAPI developers' guide

## [Development iteration](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#development-iteration)

1. write tests (see [tests' structure](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#tests-structure));
2. implement necessary feature in the library;
3. run MyPy and test (see about [running mypy and tests](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#running-mypy-and-tests));
4. push changes.

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
   
   from . import requests
   
   site_m.__dict__['requests'] = requests
   site = site_m.Site('stackoverflow')
   
   
   @lest.setup
   def reset_requests() -> None:
       requests.reset()
   ```
3. then, there should be the following methods:
    + `test_get_answers_without_ids` - tests that method `get_answers` without transmitting identifiers to it applies to the desired URL;
    + `test_get_answers_with_ids` - tests that method `get_answers` with transmitting some identifiers to it applies to the desired URL;
    + `test_return_value_of_get_answers` - tests that method `get_answers` returns desired list of class `Item`'s instances (desired is `[Item({'id': 1})]`);
    + `test_get_answer` - tests that method `get_answer` applies to the desired URL;
    + `test_return_value_of_get_answer` - tests that method `get_answer` returns desired instance of class `Item` (desired is `Item({'id': 1})`).

For more details, see file [`tests/test_client/test_get_answers.py`](https://github.com/wchistow/pystackapi/blob/master/tests/test_client/test_get_answers.py).

---

## [Running MyPy and tests](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md#running-mypy-and-tests)

1. Install requirements of library from file `requirements.txt`:
   ```shell
   pystackapi$ pip install -r ./requirements.txt
   ``` 
2. Install special requirements for running MyPy:
   ```shell
   pystackapi$ pip install mypy
   pystackapi$ pip install types-requests
   ```
3. Run, directly, MyPy:
   ```shell
   pystackapi$ python -m mypy ./src/
   ```
4. Install requirements for running tests:
   ```shell
   pystackapi$ pip install lest rich==13.4.2  # Rich is requirement of Lest
   ```
5. Run tests:
   ```shell
   pystackapi$ cd tests
   pystackapi/tests$ python main.py
   ```

> Note #1: if you already installed all requirements, you can run MyPy and tests by command
> ```shell
> pystackapi$ python -m mypy ./src/; cd tests; python main.py
> ```

> Note #2: you can install all developer's requirements by this command:
> ```shell
> $ pip install mypy types-requests lest rich==13.4.2
> ```

---
