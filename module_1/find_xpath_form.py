from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = " http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Edge()

try:
    browser.get(link)
    browser.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Petrov")
    browser.find_element(By.XPATH, "//input[@class='form-control city']").send_keys("Smolensk")
    browser.find_element(By.XPATH, "//input[@id='country']").send_keys("Russia")

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
