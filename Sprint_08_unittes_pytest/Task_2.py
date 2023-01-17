# You have function divide
#
# Please, write the code with unit tests for the function "divide":
# minimum 3 tests
# must check all flows
# all test must be pass
# no failures
# no skip

def divide(num_1, num_2):
    return float(num_1)/num_2

import unittest


class DivideTest(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(9, 3), 3)

    def test_divide_floats(self):
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_negatives(self):
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(-1, 1), -1)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_divide_str(self):
        with self.assertRaises(TypeError):
            divide(5, '2')

    def test_divide_none(self):
        with self.assertRaises(TypeError):
            divide(3, None)


if __name__ == '__main__':
    unittest.main()
