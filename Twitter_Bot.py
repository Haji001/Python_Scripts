from logging import root

from layers_util import layers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import requests
import time


# Open chrome and maximize the window
the_service = Service("C:\\Users\Hagi\PycharmProjects\Trainings\chromedriver.exe")
driver = webdriver.Chrome(service=the_service)
driver.maximize_window()


# Go to twitter and enter username and password, and hit ENTER
driver.get("https://twitter.com/i/flow/login")
time.sleep(5)


# Create a variable for username and hit ENTER
usernameInput=driver.find_element(By.NAME,"username")
usernameInput.send_keys("dummy_reply001")
time.sleep(5)
usernameInput.send_keys(Keys.RETURN)
time.sleep(5)


# Create a variable for password and hit ENTER
pass_input=driver.find_element(By.NAME,"password")
pass_input.send_keys("1234%^&*")
pass_input.send_keys(Keys.RETURN)
time.sleep(5)


# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

def like_tweet(hashtag):
    driver.get('https://twitter.com/search?q='+hashtag+'&src=typd')
    time.sleep(5)
    for i in range(1,4):
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
      time.sleep(3)



like_tweet("webflow")

