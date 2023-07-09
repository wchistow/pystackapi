# PyStackAPI

> **Warning:** This library is currently under development!

## What is PyStackAPI?

PyStackAPI is a modern, 100% typed wrapper for the StackExchange API, written in Python.

## Simple example

Getting general information about site:

```python
from pystackapi import Site
from pystackapi.sites import StackOverflow

site = Site(StackOverflow)

info = site.get_info()

print(f'Total questions on StackOverflow: {info.total_questions}')
```

Output:

```text
Total questions in StackOverflow: 23789952
```
