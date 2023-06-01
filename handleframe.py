from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://londonfreelance.org/courses/frames/index.html")
driver.switch_to.frame('main')
head = driver.find_element(By.CSS_SELECTOR,'body h2')
print(head)
