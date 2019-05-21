# -*- coding: utf-8 -*-

""" sample/tests/utils/test_hello.py """

import sample.utils.hello


def test_greeting():
    """ getGreeting() should return 'Привет!' """
    assert sample.utils.hello.get_greeting() == 'Привет!'
