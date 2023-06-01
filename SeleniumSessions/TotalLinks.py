from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/")
linklist = driver.find_element(By.TAG_NAME,'img')
for ele in linklist:
    print(ele.get_attribute('src'))