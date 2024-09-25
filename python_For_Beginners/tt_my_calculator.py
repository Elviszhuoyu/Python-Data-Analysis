import unittest
from my_calculator import my_adder

class TestMyaAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(5,3),8)

    def test_negative_with_negative(self):
        self.assertEqual(my_adder(-5, 3), -2)
