import unittest

from add import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(10, 0), 10)
        self.assertEqual(add(-2, 8), 4)

if __name__ == '__main__':
    unittest.main()
