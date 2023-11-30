from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("a")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("b")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("b@a")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    attach_file = browser.find_element(By.NAME, "file")
    attach_file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()