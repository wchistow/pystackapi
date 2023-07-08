# PyStackAPI developers' guide

In first, do some changes (I am not describing the creation of a fork, etc., I think you now it);

---

Then, run MyPy and tests:

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

> Note: if you already installed all requirements, you can run MyPy and tests by command
> ```shell
> pystackapi$ python -m mypy ./src/; cd tests; python main.py
> ```

---

Finally, push changes.
