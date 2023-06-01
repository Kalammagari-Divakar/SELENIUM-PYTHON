from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/' )
print(driver.title)
driver.find_element(By.ID,'Form_getForm_subdomain').send_keys('divakar selenium')
driver.find_element(By.ID,'Form_getForm_Name').send_keys('kalammagari divakar')
driver.find_element(By.ID,'Form_getForm_Email').send_keys('kdivakar2000@gmail.com')
driver.find_element(By.ID,'Form_getForm_Contact').send_keys('6302414526')
driver.find_element(By.ID,'Form_getForm_Country').send_keys('india')
driver.find_element(By.ID,'Form_getForm_action_submitForm').click()
time.sleep(5)

