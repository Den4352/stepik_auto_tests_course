from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)    
    
    # Нажатие на кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    
    # Запоминаем название второй вкладки
    new_window = browser.window_handles[1] # Название второй вкладки

    # Переход на вкладку 
    browser.switch_to.window(new_window) # Переход на вкладку 
    new_window = browser.window_handles[1] # Название второй вкладки

    # Выбор елемента x и вычисление капчи 
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    y = calc(x)

    # Вывод решения капчи в поле ответа 
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    # Нажатие на кнопку
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
    
    
    # Переходы по вкладкам
    # browser.switch_to.window(new_window) - Переход на вкладку 
    # new_window = browser.window_handles[1] - Название второй вкладки
    # first_window = browser.window_handles[0]