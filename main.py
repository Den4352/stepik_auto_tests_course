import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
        input2.send_keys("Ivan")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third")
        input3.send_keys("Ivan")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "test 1 done succesfull")


    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
        input2.send_keys("Ivan")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third")
        input3.send_keys("Ivan")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "test 1 done succesfull")


if __name__ == "__main__":
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
