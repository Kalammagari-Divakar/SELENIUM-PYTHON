import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.saucedemo.com/')
print(driver.title)
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.NAME, 'login-button').click()
driver.find_element(By.XPATH,"//button[text()='Add to cart']").click()
driver.get('https://www.saucedemo.com/cart.html')
time.sleep(4)
driver.find_element(By.ID,'remove-sauce-labs-backpack').click()
assert driver.find_element(By.CLASS_NAME, 'inventory_item_name').is_displayed()==False
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='btn btn_secondary back btn_medium']").click()
driver.quit()