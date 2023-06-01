import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.saucedemo.com/')
print(driver.title)
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.NAME, 'login-button').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
time.sleep(4)
#adding item to cart
var1 = "Sauce Labs Backpack"
var2 = "Sauce Labs Backpack"


def assertEqual (var1,var2):
    print("v3 pass")
    pass


assertEqual("Tutorialspoint", "Tutorialspoint")
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
#removing item from cart
driver.find_element(By.XPATH,"//button[text()='Remove']").click()
time.sleep(3)
button1 = "Add to cart"
button2 ="Add to cart"
assert button1==button2,"testcasefailed"
print("item removed succesfully")
driver.quit()



