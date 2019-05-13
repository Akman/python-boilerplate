from unittest import TestCase
from sample.hello import run

class TestHello(TestCase):
    def test_basic(self):
        s = run()
        self.assertTrue(isinstance(s, str))
