# ![](logo.png)

Here is PyStackAPI version 0.1.0

## What is PyStackAPI?

PyStackAPI is a modern, 100% typed wrapper for the StackExchange API, written in Python.

## Installing

To install PyStackAPI, just enter in the terminal:

```shell
pip install git+https://github.com/wchistow/pystackapi.git@0.1.0
```

## Documentation

You can find documentation here: https://pystackapi.gitbook.io/docs.

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
