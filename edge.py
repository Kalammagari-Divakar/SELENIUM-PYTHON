from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserName = "Edge"
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "Edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("please pass the correct browsername:"+browserName)
    raise Exception('driver is not found')
driver.implicitly_wait(5)
driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')
driver.find_element(By.ID,'username').send_keys('kdivakar2000@gmail.com')
driver.find_element(By.ID,'password').send_keys('Diwi@202127')
driver.find_element(By.XPATH,"//button[text()='Sign in']").click()
time.sleep(3)
driver.quit()