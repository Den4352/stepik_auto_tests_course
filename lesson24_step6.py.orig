<<<<<<< HEAD
=======
from selenium import webdriver
>>>>>>> cc12ce9 (Уроки stepik до 3-го блока)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
<<<<<<< HEAD
=======
import time
>>>>>>> cc12ce9 (Уроки stepik до 3-го блока)
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 5).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "$100")
<<<<<<< HEAD
    )
=======
    )   
>>>>>>> cc12ce9 (Уроки stepik до 3-го блока)
print(price)
button = browser.find_element(By.CSS_SELECTOR, "#book")
button.click()

# Выбор елемента x и вычисление капчи 
<<<<<<< HEAD
a_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
a = int(a_element.text)
y = calc(a)
=======
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = int(x_element.text)
y = calc(x)
>>>>>>> cc12ce9 (Уроки stepik до 3-го блока)
# Вывод решения капчи в поле ответа 
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)
# Нажатие на кнопку
button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
button2.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
# закрываем браузер после всех манипуляций
# browser.quit()




# Настройка ожиданий
# time.sleep(1) - задержка страницы 1 сек

# browser.implicitly_wait(5) - говорим WebDriver искать каждый элемент в течение 5 секунд "неяаное ожидание"

# button = WebDriverWait(browser, 5).until(
        # EC.element_to_be_clickable((By.ID, "verify"))
    # ) - element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.

# button = WebDriverWait(browser, 5).until_not(
        # EC.element_to_be_clickable((By.ID, "verify"))
    # )