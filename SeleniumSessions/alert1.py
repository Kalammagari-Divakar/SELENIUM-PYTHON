from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://the-internet.herokuapp.com/javascript_alerts")
#wait = WebDriverWait(driver,10)
#element1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='Click for JS Alert']")))
#element1.click()
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
ele = driver.switch_to.alert
print(ele.text)
ele.accept()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
ele2 = driver.switch_to.alert
time.sleep(4)
ele2.send_keys('divi')
ele2.accept()
#print(ele2.text)
#ele2.dismiss()
time.sleep(3)