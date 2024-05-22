"""Tests for get-methods of class `Chat`."""
import lest

from pystackapi import chat as chat_m
from pystackapi import Chat

from main import chatexchange

chat_m.__dict__['chatexchange'] = chatexchange
chat = Chat()


@lest.setup
def reset_chatexchange() -> None:
    chatexchange.reset()


# some tests...
