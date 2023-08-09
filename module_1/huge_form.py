from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Edge()

try:
    browser.get(link)
    elements = browser.find_elements(By.XPATH, "//input[@type='text']")
    for element in elements:
        element.send_keys('fake_value')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
