import unittest


class TestYams(unittest.TestCase):
    def test_one_plus_one(self):
        one_plus_one=1+1
        self.assertEqual(one_plus_one, 2)


if __name__ == '__main__':
    unittest.main()