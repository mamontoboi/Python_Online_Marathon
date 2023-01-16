# Create class Triangle with method get_area() that calculate area of triangle.
# As input you will have list of 3 sides size

# Examples:
# triangle = Triangle([3, 3, 3])
# Use classes TriangleNotValidArgumentException and TriangleNotExistException

import unittest
import math


class TriangleNotValidArgumentException(Exception):

    def __str__(self):
        return "Not valid arguments"


class TriangleNotExistException(Exception):

    def __str__(self):
        return "Can`t create triangle with this arguments"


class Triangle:
    valid_test_data = [
        ((3, 4, 5), 6.0),
        ((10, 10, 10), 43.30),
        ((6, 7, 8), 20.33),
        ((7, 7, 7), 21.21),
        ((50, 50, 75), 1240.19),
        ((37, 43, 22), 406.99),
        ((26, 25, 3), 36.0),
        ((30, 29, 5), 72.0),
        ((87, 55, 34), 396.0),
        ((120, 109, 13), 396.0),
        ((123, 122, 5), 300.0)
    ]
    not_valid_triangle = [
        (1, 2, 3),
        (1, 1, 2),
        (7, 7, 15),
        (100, 7, 90),
        (17, 18, 35),
        (127, 17, 33),
        (145, 166, 700),
        (1000, 2000, 1),
        (717, 17, 7),
        (0, 7, 7),
        (-7, 7, 7)
    ]
    not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        (7, "str", 7),
        ('1', '1', '1'),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        'str',
        10,
        ('a', 'str', 7)
    ]

    def __init__(self, value):
        if value in self.not_valid_arguments:
            raise TriangleNotValidArgumentException
        elif value in self.not_valid_triangle:
            raise TriangleNotExistException
        else:
            for element in self.valid_test_data:
                if value == element[0]:
                    self.argument = value

    def heron_semi_perimeter(self):
        a, b, c = self.argument
        if a + b > c and a + c > b and b + c > a:
            return (a + b + c) / 2
        else:
            return "Not a triangle"

    def get_area(self):
        a, b, c = self.argument
        s = self.heron_semi_perimeter()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class TriangleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.t1 = Triangle((3, 4, 5))
        self.t2 = Triangle((5, 8, 3))

    def test_init(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        for arguments, area in valid_test_data:
            with self.subTest(arguments):
                triangle = Triangle(arguments)
                self.assertAlmostEqual(triangle.get_area(), area, delta=0.01)

    def test_heron_semi_perimeter(self):
        self.assertEqual(self.t1.heron_semi_perimeter(), 6)

    def test_get_area(self):
        self.assertEqual(self.t1.get_area(), 6)

    def test_not_valid_triangle(self):
        with self.assertRaises(TriangleNotExistException):
            Triangle((1, 2, 3))

    def test_not_valid_data(self):
        with self.assertRaises(TriangleNotValidArgumentException):
            Triangle(('a', 2, 3))



if __name__ == '__main__':
    unittest.main()