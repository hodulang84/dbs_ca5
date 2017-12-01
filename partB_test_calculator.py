#CA5 last updated on 30/11/2017
#10359541 Seungmin Back

import unittest
from partB_Calculator import Calculator

# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

# map, lambda
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(1,1)
        self.assertEqual(2, result)
        result = self.calc.add([1,2,3],[1,2,3])
        self.assertEqual([2,4,6], result)

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(1,1)
        self.assertEqual(0, result)
        result = self.calc.subtract([1,2,3],[1,2,3])
        self.assertEqual([0,0,0], result)

    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply(10,5)
        self.assertEqual(50, result)
        result = self.calc.multiply([1,2,3],[1,2,3])
        self.assertEqual([1,4,9], result)

    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide(10,5)
        self.assertEqual(2, result)
        result = self.calc.divide([1,2,3],[1,2,3])
        self.assertEqual([1,1,1], result)

#filter, lambda          
    def test_calculator_list_exponent_is_even_method_returns_correct_result(self):
        result = self.calc.list_exponent_is_even([1,2,3],[4,5,6])
        self.assertEqual([32], result)

#reduce, lambda
    def test_calculator_list_sum_method_returns_correct_result(self):
        result = self.calc.list_sum([1,2,3,4,5])
        self.assertEqual(15, result)

    def test_calculator_list_max_method_returns_correct_result(self):
        result = self.calc.list_max([1,2,3,4,5])
        self.assertEqual(5, result)

    def test_calculator_list_min_method_returns_correct_result(self):
        result = self.calc.list_min([1,2,3,4,5])
        self.assertEqual(1, result)

#list comprehension
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square(3)
        self.assertEqual(9, result)
        result = self.calc.square([1,2,3,4,5])
        self.assertEqual([1,4,9,16,25], result)

    def test_calculator_factorial_method_returns_correct_result(self):
        result = self.calc.factorial(10)
        self.assertEqual(3628800, result)
        result = self.calc.factorial([1,2,3,4,5])
        self.assertEqual([1,2,6,24,120], result)

if __name__ == '__main__':
    unittest.main()
