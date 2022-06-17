from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)


    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.CSS_SELECTOR,'.btn.btn-primary')
    button.click()

    time.sleep(1)
    browser.switch_to.window(browser.window_handles[1])
    print(browser.window_handles[1])


    x = browser.find_element(By.ID, 'input_value')
    x=int(x.text)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(calc(x)))

    button = browser.find_element(By.CSS_SELECTOR,'.btn.btn-primary')
    button.click()

    time.sleep(1)
    # Отправляем заполненную форму

   # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()