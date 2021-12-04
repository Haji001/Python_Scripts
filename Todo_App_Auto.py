# Implementation of Selenium WebDriver with Python using PyTest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_lambdatest_todo_app():


    the_service = Service("C:\\Users\Hagi\PycharmProjects\Trainings\chromedriver.exe")
    driver = webdriver.Chrome(service=the_service)
    driver.maximize_window()

    driver.get('https://lambdatest.github.io/sample-todo-app/')
    driver.maximize_window()

    driver.find_element(By.NAME,"li1").click()
    driver.find_element(By.NAME,"li2").click()

    title = "Sample page - lambdatest.com"
    assert title == driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = driver.find_element(By.ID,"sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)

    driver.find_element(By.ID,"addbutton").click()
    sleep(5)

    output_str = driver.find_element(By.NAME,"li6").text
    sys.stderr.write(output_str)

    sleep(2)
    driver.close()
test_lambdatest_todo_app()