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

response = site.get_info()

info = response['items'][0]

print(f'Total questions in StackOverflow: {info.total_questions}')
```

Output:

```text
Total questions in StackOverflow: 23789952
```
