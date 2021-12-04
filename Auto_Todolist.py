from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

s = Service("C:\\Users\Hagi\PycharmProjects\Python_Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://simplest-react-todo-app.herokuapp.com/")
time.sleep(5)

#driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/ul/li[1]/div/label/input").click()
#time.sleep(5)

textInput = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/header/input")
textInput.send_keys("First Try")
time.sleep(6)

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/footer/div[1]/div/a[1]").click()
time.sleep(6)

driver.save_screenshot('new_screenshot.png')
driver.quit()

