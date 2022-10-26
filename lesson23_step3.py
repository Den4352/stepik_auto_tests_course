from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
   
    # Нажатие на кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    
    # Принятие confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    
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
    
    
    # Alerts
    
    # alert
    # alert = browser.switch_to.alert - Выбор модалки alert 
    # alert.accept() - Принятие alert
    # alert_text = alert.text - Получение текста из alert
    
    # confirm
    # confirm = browser.switch_to.alert - Выбор модалки confirm
    # confirm.accept() - Принятие confirm
    # confirm.dismiss() - Отказ confirm
    
    # prompt
    # prompt = browser.switch_to.alert - Выбор модалки prompt
    # prompt.send_keys("My answer") - Ввод текста в модалку prompt
    # prompt.accept() - Принятие promt
    