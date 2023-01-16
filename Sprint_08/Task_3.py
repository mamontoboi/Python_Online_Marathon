# Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation without a
# complex solution.
#
# Write unit tests for this function with QuadraticEquationTest class
#
# Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0

import unittest
import cmath


def quadratic_equation(a, b, c):
    try:
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant > 0:
            root_1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
            root_2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
            return root_2.real, root_1.real
        elif discriminant == 0:
            return -b / (2 * a)
        else:
            return None
    except ZeroDivisionError:
        raise ValueError



# print(quadratic_equation(1, 8, 12))
# print(quadratic_equation(5, 3, 7))
# print(quadratic_equation(1, 6, 9))
# print(quadratic_equation(0, 3, 5))
# print(quadratic_equation("3", 3, 5))

#
class QuadraticEquationTest(unittest.TestCase):
    def test_quadratic_equation_d_positive(self):
        self.assertEqual(quadratic_equation(1, 8, 12), (-2.0, -6.0))

    def test_quadratic_equation_d_negative(self):
        self.assertEqual(quadratic_equation(5, 3, 7), None)

    def test_quadratic_equation_d_zero(self):
        self.assertEqual(quadratic_equation(1, 6, 9), -3.0)

    def test_quadratic_equation_type_err(self):
        with self.assertRaises(TypeError):
            quadratic_equation("3", 3, 5)


if __name__ == '__main__':
    unittest.main()

