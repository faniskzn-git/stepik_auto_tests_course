from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math




link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Edge()
number = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser.get(link)
    # поиск элемента по части ссылки и нажатие
    browser.find_element(By.PARTIAL_LINK_TEXT, number).click()

    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
