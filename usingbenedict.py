from benedict import benedict
obj=benedict.from_yaml('C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\beni.yaml')
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get(obj['rest.url'])
time.sleep(3)
driver.find_element(By.ID,'user-name').send_keys(obj['rest.login'])


time.sleep(3)