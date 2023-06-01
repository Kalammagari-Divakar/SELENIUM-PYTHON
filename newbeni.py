import time

from benedict import benedict
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

obj=benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\newbeni.yaml")
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
browserName =obj['rest.browser']
print(browserName)
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "Edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("please pass the correct browsername:")
    raise Exception('driver is not found')
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get(obj['rest.url'])
driver.find_element(By.ID,'user-name').send_keys(obj['rest.user'])
driver.find_element(By.ID,'password').send_keys(obj['rest.pass'])
driver.find_element(By.ID,'login-button').click()
abc="//button[text()='{}']".format(obj['rest.button'])
print(abc)
driver.find_element(By.XPATH,abc).click()
time.sleep(3)
#adding item to cart
var1 = "Sauce Labs Backpack"
var2 = "Sauce Labs Backpack"
assert var1==var2 ,"testcase failed"
print("validation 1 pass")
discription1 = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
discription2 = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
assert discription1==discription2,"test case failed"
print("validation 2 pass ")
price1 = 29.99
price2 = 29.99
assert price1==price2,"testcase failed"
print("validation 3 pass, item added to cart")
driver.get(obj['rest.url2'])
time.sleep(3)
driver.find_element(By.ID,'remove-sauce-labs-backpack').click()
time.sleep(3)
#removing from the cart
button1 = "Add to cart"
button2 ="Add to cart"
assert button1==button2,"testcasefailed"
print("item removed succesfully")
time.sleep(3)
driver.quit()


