""" sample/tests/utils/test_hello.py """

from unittest import TestCase
import sample.utils.hello

class TestUtilsHello(TestCase):
    """ sample.cli test case """
    def test_greeting(self):
        """ getGreeting() should return 'Привет!' """
        self.assertEqual(sample.utils.hello.get_greeting(), 'Привет!')
