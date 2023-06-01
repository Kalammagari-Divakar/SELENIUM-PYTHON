from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
browserName = "chrome"
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
driver.get('https://www.linkedin.com/login')
driver.find_element(By.ID,'username').send_keys("kdivakar2000@gmail.com")
driver.find_element(By.ID,'password').send_keys("Diwi@202127")
driver.find_element(By.XPATH,"//button[text()='Sign in']").click()
print(driver.title)
time.sleep(15)
driver.quit()



