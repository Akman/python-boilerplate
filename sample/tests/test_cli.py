""" sample/tests/test_cli.py """

from unittest import TestCase
import sample.cli

class TestCli(TestCase):
    """ sample.cli test case """
    def test_main(self):
        """ main() should return 0 """
        self.assertEqual(sample.cli.main(), 0)
