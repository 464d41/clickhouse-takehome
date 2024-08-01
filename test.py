"""Run some tests"""

import unittest

from topn.topn import Topn


class TestTopn(unittest.TestCase):
    """E2e tests"""

    def test_test_e2e_0(self):
        """
        Test the module e2e
        """
        path = "data/data5.txt"
        result = Topn(path).top(3)
        expected = [
            "http://api.tech.com/item/89169",
            "http://api.tech.com/item/71910",
            "http://api.tech.com/item/60263",
        ]
        self.assertEqual(result, expected)

    def test_test_e2e_1(self):
        """
        Test the module e2e
        """
        path = "data/data1000.txt"
        result = Topn(path).top(5)

        expected = ['http://api.tech.com/item/83488', 'http://api.tech.com/item/81914', 'http://api.tech.com/item/72053', 'http://api.tech.com/item/68160', 'http://api.tech.com/item/27971']
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
