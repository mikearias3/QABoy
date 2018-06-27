from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorScreen:

    def __init__(self, driver):
        self.driver = driver
        self.formula = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.oneplus.calculator:id/formula")))
        self.result = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.oneplus.calculator:id/result")))
        self.divide_button = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.oneplus.calculator:id/op_div")))
        self.multiply_button = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.oneplus.calculator:id/op_mul")))
        self.minus_button = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.oneplus.calculator:id/op_sub")))
        self.plus_button = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.oneplus.calculator:id/op_add")))
        self.equals_button = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.oneplus.calculator:id/eq")))
        self.delete_button = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.oneplus.calculator:id/del")))

    def click_number(self, number):
        """
        The reason behind not mapping the numbers as individual elements is because the all do a similar function and
        share a similar ID. So they can all be interacted with with a single parametrized find_element.

        :param number:
        :return:
        """
        _no = str(number)
        self.driver.instance.find_element(MobileBy.XPATH, "//android.widget.Button[contains(@text, " + _no + ")]").click()
        assert _no in self.formula.text, "Clicked number wasn't reflected."

    def click_all_numbers(self):
        for i in range(10):
            self.click_number(i)
        assert self.formula.text == "123,456,789"

    def click_delete_button(self):
        self.delete_button.click()

    def add_numbers(self, num1, num2):
        self.click_number(num1)
        self.plus_button.click()
        self.click_number(num2)
        self.equals_button.click()

        _res = num1 + num2

        assert self.result.text == str(_res)

    def substract_numbers(self, num1, num2):
        self.click_number(num1)
        self.minus_button.click()
        self.click_number(num2)
        self.equals_button.click()

        _res = num1 - num2

        assert self.result.text == str(_res)

    def multiply_numbers(self, num1, num2):
        self.click_number(num1)
        self.multiply_button.click()
        self.click_number(num2)
        self.equals_button.click()

        _res = num1 * num2

        assert self.result.text == str(_res)

    def divide_numbers(self, num1, num2):
        self.click_number(num1)
        self.divide_button.click()
        self.click_number(num2)
        self.equals_button.click()

        _res = num1 / num2

        assert self.result.text == str(_res)
