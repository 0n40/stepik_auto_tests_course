from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(link)
    time.sleep(1)

    cost = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, 'input_value')
    x=int(x.text)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(calc(x)))

    button = browser.find_element(By.ID,'solve')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()