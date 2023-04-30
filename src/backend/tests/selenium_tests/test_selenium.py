import time
import pytest

from selenium import webdriver


def test_frontend():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000')
    time.sleep(3)
    button = driver.find_element(value="start_button")
    timer = driver.find_element(value="timer")
    assert timer.text == str()
    button.click()
    time.sleep(3)
    current_time = time.time()
    assert current_time -1 <= float(timer.text) <= current_time + 1
    time.sleep(1)
    driver.close()
