import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.saucedemo.com/')
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.NAME, 'login-button').click()
time.sleep(5)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(2)
driver.refresh()
driver.quit()

