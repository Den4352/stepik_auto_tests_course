from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    

    # Ваш код, который заполняет обязательные поля
        
    label = browser.find_element(By.CSS_SELECTOR, "label")
    browser.execute_script("return arguments[0].scrollIntoView(true);", label)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    y = calc(x)
    print(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    
     

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()