# -*- coding: utf-8 -*-

import sys
from importlib import import_module
import pytest
from helper import MockBot

not_implemented = pytest.mark.xfail(reason="test not implemented/complete")

def test_hello(monkeypatch):

    bot = MockBot()

    monkeypatch.setattr('slackbot.bot.listen_to', bot.mock_listen_to)
    monkeypatch.setattr('slackbot.bot.respond_to', bot.mock_respond_to)

    sys.path.append("plugins")
    import_module("hello_world")

    r = bot.respond("Hello, world.")
    assert r[0]['msg'] == 'reply'
    assert r[0]['text'] == 'Hello yourself!'
    assert r[1]['msg'] == 'react'
    assert r[1]['emojiname'] == 'robot_face'

    r = bot.listen("Hello, world.")
    assert r[0]['msg'] == 'send'
    assert r[0]['text'] == 'Hello everyone!'
    assert r[1]['msg'] == 'react'
    assert r[1]['emojiname'] == 'eggplant'
