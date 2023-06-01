from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
browserName = "Firefox"
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "Safari":
    driver = webdriver.Safari()
else:
    print("please pass the correct browsername:"+browserName)
    raise Exception('driver is not found')
driver.implicitly_wait(5)
driver.get('https://www.facebook.com/')
driver.find_element(By.ID,'email').send_keys('6302414526')
driver.find_element(By.ID,'pass').send_keys('Diwi@202127')
driver.find_element(By.XPATH,"//button[@id='u_0_5_9v']").click()
time.sleep(3)
driver.quit()