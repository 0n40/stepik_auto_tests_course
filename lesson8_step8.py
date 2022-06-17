from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)


    # Ваш код, который заполняет обязательные поля
    firstname = browser.find_element(By.CSS_SELECTOR,'[name="firstname"]')
    firstname.send_keys("Boris")

    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lastname.send_keys("Blade")

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys("withlove@russia.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'input.txt')  # добавляем к этому пути имя файла

    file = browser.find_element(By.CSS_SELECTOR, '#file')
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
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