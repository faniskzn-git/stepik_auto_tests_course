from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# link = "https://suninjuly.github.io/selects1.html"
link = "https://suninjuly.github.io/selects2.html"


def calc(x, y):
    return str(int(x) + int(y))


try:
    browser = webdriver.Edge()
    browser.get(link)

    # код, который заполняет обязательное поле
    x_element = browser.find_element(By.XPATH, "//span[@id='num1']").text
    y_element = browser.find_element(By.XPATH, "//span[@id='num2']").text
    answer = calc(x_element, y_element)

    # код, который выберет из списка нужное значение
    select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(answer)

    # Отправляем заполненную форму
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
