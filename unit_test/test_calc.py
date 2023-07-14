import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add_func(self):
        # Method 1:
        # result = test_func.add(10,5)
        #Method 2:
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

        # We can test the test is failing here:
        # self.assertEqual(result, 16)

    def test_subtract_func(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply_func(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide_func(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        #expections testing method: Not preferred
        # self.assertRaises(ValueError, test_func.divide, 10,0)

        #Preferred method
        with self.assertRaises(ValueError):
            calc.divide(10,0)


# We can use this condition instead of using "python -m unittest test_func.py"
if __name__ == '__main__':
    unittest.main()
