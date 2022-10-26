from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(num1_Num, num2_Num):
  return str(num1_Num+num2_Num)
  
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1_Num = int(num1.text)
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2_Num = int(num2.text)
    y = calc(num1_Num, num2_Num)
    print(y)
    
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y) # ищем элемент с текстом "Python"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    # input1.send_keys(y)
    # input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    # input2.click()
    # input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    # input3.click()

    # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()