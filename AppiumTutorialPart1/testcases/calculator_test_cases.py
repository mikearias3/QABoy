import unittest

from pageobjects.calculator_screen import CalculatorScreen
from webdriver.webdriver import Driver


class CalculatorTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_calculator_launches(self):
        calculator = CalculatorScreen(self.driver)
        calculator.click_number(8)
        calculator.click_delete_button()
        calculator.click_all_numbers()

    def test_calculator_sum(self):
        calculator = CalculatorScreen(self.driver)
        calculator.add_numbers(5, 6)

    def test_calculator_substraction(self):
        calculator = CalculatorScreen(self.driver)
        calculator.substract_numbers(6, 5)

    def test_calculator_multiply(self):
        calculator = CalculatorScreen(self.driver)
        calculator.multiply_numbers(6, 5)

    def test_calculator_divide(self):
        calculator = CalculatorScreen(self.driver)
        calculator.divide_numbers(6, 5)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)