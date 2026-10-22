import random
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This runs automatically before every test method
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 99)

    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2.0)
        # Pin float return type explicitly
        result_float = self.calc.divide(7, 2)
        self.assertEqual(result_float, 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_modulo(self):
        result = self.calc.modulo(5, 3)
        self.assertEqual(result, 2)

    def test_modulo_negative_operand(self):
        result = self.calc.modulo(-7, 3)
        self.assertEqual(result, 2)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)

    def test_power(self):
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)

    def test_power_zero_to_zero(self):
        result = self.calc.power(0, 0)
        self.assertEqual(result, 1)

    def test_power_negative_exponent(self):
        result = self.calc.power(2, -1)
        self.assertEqual(result, 0.5)

    def test_properties_randomized(self):
        # Extra credit: Property-based testing over 100 random iterations
        for _ in range(100):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            
            # Property: subtract(add(a, b), b) == a
            self.assertEqual(self.calc.subtract(self.calc.add(a, b), b), a)
            
            # Property: multiply(a, b) == multiply(b, a)
            self.assertEqual(self.calc.multiply(a, b), self.calc.multiply(b, a))

if __name__ == "__main__":
    unittest.main()