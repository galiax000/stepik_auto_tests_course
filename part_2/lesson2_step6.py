from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(answer)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()