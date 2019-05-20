""" sample/tests/utils/test_hello.py """

import pytest
import sample.utils.hello

def test_greeting():
    """ getGreeting() should return 'Привет!' """
    assert sample.utils.hello.get_greeting() == 'Привет!'
