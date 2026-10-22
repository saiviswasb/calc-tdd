import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This runs automatically before every test method
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_power(self):
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)

    def test_divide(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2.0)

    def test_modulo(self):
        result = self.calc.modulo(5, 3)
        self.assertEqual(result, 2)

    def test_modulo_negative_operand(self):
        result = self.calc.modulo(-7, 3)
        self.assertEqual(result, 2)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()