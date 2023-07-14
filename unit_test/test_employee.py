
import unittest
#For Mocking purpose to test the functionalities while the website or server is down.
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self): #Method 2 - setUp Function
        print('setUp')
        self.emp_1 = Employee('Mohammed', 'Adam', 25000)
        self.emp_2 = Employee('Mani', 'Kandan', 35000)

    def tearDown(self):
        print('tearDown\n')


    def test_email(self):
        #Method 1 for every functions we can use this method or else we can use the seperate "setUp" function
        # emp_1 = Employee('Mohammed', 'Adam', 25000)
        # emp_2 = Employee('Mani', 'Kandan', 35000)

        print('test_email')
        self.assertEqual(self.emp_1.email, 'Mohammed.Adam@email.com')
        self.assertEqual(self.emp_2.email, 'Mani.Kandan@email.com')

        self.emp_1.first = 'Williams'
        self.emp_2.first = 'Vignesh'

        self.assertEqual(self.emp_1.email, 'Williams.Adam@email.com')
        self.assertEqual(self.emp_2.email, 'Vignesh.Kandan@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Mohammed Adam')
        self.assertEqual(self.emp_2.fullname, 'Mani Kandan')

        self.emp_1.first = 'Williams'
        self.emp_2.first = 'Vignesh'

        self.assertEqual(self.emp_1.fullname, 'Williams Adam')
        self.assertEqual(self.emp_2.fullname, 'Vignesh Kandan')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 26250)
        self.assertEqual(self.emp_2.pay, 36750)


    def test_monthly_schedule(self):

        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Adam/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Kandan/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()
