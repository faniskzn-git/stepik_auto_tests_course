from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Edge()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    # код, который заполняет обязательное поле
    valuex_atr = browser.find_element(By.XPATH, "//img[@id='treasure']").get_attribute("valuex")
    answer = calc(valuex_atr)
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(answer)

    # код, который проставит нужные чекбокс и радиокнопку
    browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()

    # Отправляем заполненную форму
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
