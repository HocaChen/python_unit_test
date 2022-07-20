import unittest
import Math

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Math.add(2,2), 4)  # add assertion here

    def test_multiply(self):
        self.assertEqual(Math.multiply(2,2), 4)  # add assertion here

    def test_divide(self):
        self.assertRaises(ValueError, Math.divide, 2, 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
