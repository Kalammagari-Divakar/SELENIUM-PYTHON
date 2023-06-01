from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://classic.crmpro.com/index.html')
time.sleep(3)
user = driver.find_element(By.NAME,'username')
pswrd = driver.find_element(By.NAME,'password')
login = driver.find_element(By.XPATH,"//input[@class='btn btn-small']")
act_chains = ActionChains(driver)
act_chains.send_keys_to_element(user,'divakar').perform()
act_chains.send_keys_to_element(pswrd,'123@').perform()
act_chains.click(login).perform()
time.sleep(2)
driver.quit()