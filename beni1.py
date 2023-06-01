import yaml
from benedict import benedict
obj=benedict.from_yaml('C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\beni.yaml')
#with open('beni.yaml', 'r') as file:
 #   prime_service = yaml.safe_load(file)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
#driver.get(prime_service['rest']['url'])
driver.get(obj['rest.url'])
time.sleep(3)
#driver.find_element(By.ID,'user-name').send_keys(prime_service['rest']['login'])
driver.find_element(By.ID,'user-name').send_keys(obj['rest.login'])
time.sleep(3)
#print(prime_service['rest'],['url'])
#print(prime_service['rest']['url'])


