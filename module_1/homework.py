from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Edge()

try:
    #
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.XPATH, "//div[label='First name*']/input").send_keys("Ivan")
    browser.find_element(By.XPATH, "//div[label='Last name*']/input").send_keys("Petrov")
    browser.find_element(By.XPATH, "//div[label='Email*']/input").send_keys("fakeaccount@mail.ru")

    # Отправляем заполненную форму
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()
