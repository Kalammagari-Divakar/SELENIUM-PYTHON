from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('http://automationpractice.com/index.php')
print(driver.title)
driver.find_element(By.LINK_TEXT,'Contact us').click()
ele = driver.find_element(By.ID,'id_contact')
drp = Select(ele)
time.sleep(2)
drp.select_by_index(1)