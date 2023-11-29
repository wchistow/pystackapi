"""Tests for method `Site.add_comment`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.item import Item

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow', access_token='someaccesstoken', app_key='someappkey')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_add_comment_url() -> None:
    site.add_comment(1, 'This is a test comment.')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'posts/1/comments/add')
    lest.assert_eq(requests.data, {'site': 'stackoverflow', 'access_token': 'someaccesstoken',
                                   'key': 'someappkey', 'body': 'This is a test comment.'}
                   )


@lest.register
def test_add_comment_return_value() -> None:
    res = site.add_comment(1, 'This is a test comment.')

    lest.assert_eq(res, Item({'id': 1}))
