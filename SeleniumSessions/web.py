from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\uif48567\\Documents\\drivers\\chromedriver.exe")

driver.implicitly_wait(5)
driver.get("http://www.google.com")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("Divakar automationlabs")
optionList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionList))

for ele in optionList:
    print(ele.text)
    if ele.text=="automationlabs linkedin":
        ele.click()
        break

time.sleep(5)
driver.quit()