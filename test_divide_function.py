import unittest
from divide_function import divide, NotANumber


class DivideFunction(unittest.TestCase):

    # VALID TEST CASE – assertEqual
    def test_divide_valid_10_5(self):
        self.assertEqual(2, divide(10, 5))

    # VALID TEST CASE - assertTrue
    def test_divide_valid_1000_20(self):
        self.assertTrue(50, divide(1000, 20))

    # VALID TEST CASE – ZeroDivisionError os raised when number is divided by 0
    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)

    # INVALID TEST CASE – assertRaises(TypeError)
    def test_divide_invalid(self):
        with self.assertRaises(NotANumber):
            divide("10", "5")

    # INVALID TEST CASE – Negative denominator Int
    def test_negative_denominator(self):
        with self.assertRaises(NotANumber):
            divide(5, "h")

    # VALID BOUNDARY TEST CASE
    def test_zero_numerator(self):
        self.assertEqual(0, divide(0, 5))

    # INVALID BOUNDARY TEST CASE – Using built-in ZeroDivisionError
    def test_small_denominator(self):
        numerator = 3
        denominator = 0.001
        result = divide(3, denominator)
        self.assertTrue(result > numerator)


if __name__ == '__main__':
    unittest.main()
