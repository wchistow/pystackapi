# ![](logo.png)

Here is PyStackAPI version 0.1.1

## What is PyStackAPI?

PyStackAPI is a modern, 100% typed wrapper for the StackExchange API, written in Python.

## Installing

To install PyStackAPI, just enter in the terminal:

```shell
pip install git+https://github.com/wchistow/pystackapi.git@0.1.1
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
Total questions on StackOverflow: 23789952
```

## Changelog

You can find the changelog for the PyStackAPI library in file [CHANGELOG.md](https://github.com/wchistow/pystackapi/blob/master/CHANGELOG.md).

## Contributing

Want to contribute? 

1. fork this repository;
2. do something with code (see [developers' guide](https://github.com/wchistow/pystackapi/blob/master/CONTRIBUTING.md));
3. create pull request.
