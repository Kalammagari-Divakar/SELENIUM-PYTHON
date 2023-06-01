from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.spicejet.com/')
time.sleep(3)
#move to element
ele=driver.find_element(By.XPATH,"//div[text()='Add-ons']")
act_chains=ActionChains(driver)
act_chains.move_to_element(ele).perform()
driver.find_element(By.XPATH,"//div[text()='SpiceMAX']").click()
time.sleep(3)
driver.quit()