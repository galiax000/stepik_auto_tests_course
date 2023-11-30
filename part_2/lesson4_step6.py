from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem = browser.find_element(By.ID, "moto")
    print(elem.get_attribute('title'))

    button = browser.find_element(By.ID, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()