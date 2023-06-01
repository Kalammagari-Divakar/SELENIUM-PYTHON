import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options=webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(10)
driver.get('https://www.saucedemo.com/')
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.NAME, 'login-button').click()
time.sleep(3)
#driver.get_screenshot_as_file('div_1.png');
'''full screenshot'''
#make sure that you are running in a headless browser
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element_by_tag_name('body').screenshot("tutorialspoint.png")
#driver.get_screenshot_as_file("raj.png")