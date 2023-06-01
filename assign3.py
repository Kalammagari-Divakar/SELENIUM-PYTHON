import time
from tokenize import String

# import element as element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions
from benedict import benedict

driver = webdriver.Chrome(ChromeDriverManager().install())
obj = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\ass.yaml")
s1=obj['rest.browser']
s2=str.casefold(s1)
browserName = s2
print(browserName)
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "edge":

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("please pass the correct browsername:")
driver.implicitly_wait(10)
driver.get(obj['rest.url'])
driver.find_element(By.ID, 'user-name').send_keys(obj['rest.user'])
driver.find_element(By.ID, 'password').send_keys(obj['rest.pass'])
driver.find_element(By.ID, 'login-button').click()
l = obj['rest.item1']
print(l)
i=obj['rest.item1']
#for i in l:

if i == "Sauce Labs Backpack":
    abc = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//button".format(
        obj['rest.item1'])
    print(abc)
    wait=WebDriverWait(driver,10)
    element=wait.until(expected_conditions.element_to_be_clickable((By.XPATH,abc)))
    #driver.find_element(By.XPATH, abc).click()
    element.click()
    title1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_label']//div[text()='Sauce Labs Backpack']").text
    #print(title1.text)

    discription1=driver.find_element(By.XPATH,"//div[text()='Sauce Labs Backpack']//ancestor::div[@class='inventory_item_label']//div[@class='inventory_item_desc']")
    print(discription1.text)
    price1=driver.find_element(By.XPATH,"//div[text()='Sauce Labs Backpack']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//div")
    print(price1.text)
    #price_2 = "//div[text()='{}']//ancestor::div[@class='cart_item_label']//following-sibling::div[@class='item_pricebar']//div[@class='inventory_item_price']".format(
        #obj['rest.item1'])
   # price2 = driver.find_element(By.XPATH, price_2)
    #print(price2.text)

    assert title1==obj['rest.item1'],"validationfail"
    print("pass")
    after_removing_item_from_cart = driver.find_elements(By.XPATH, "//div[@class='cart_item']"
                                                                   "/child::div[@class='cart_item_label']"
                                                                   "/child::a/child::div")
    print(after_removing_item_from_cart)

    time.sleep(3)


elif i == "Sauce Labs Bike Light":
    abc = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//button".format(
        obj['rest.item2'])
    print(abc)
    driver.find_element(By.XPATH, abc).click()
    title2 = driver.find_element(By.XPATH, "//div[@class='inventory_item_label']//div[text()='Sauce Labs Bike Light']")
    print(title2.text)
    discription2 = driver.find_element(By.XPATH,"//div[text()='Sauce Labs Bike Light']//ancestor::div[@class='inventory_item_label']//div[@class='inventory_item_desc']")
    print(discription2.text)
    price2= driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bike Light']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//div")
    print(price2.text)

    time.sleep(3)
elif i == "Sauce Labs Bolt T-Shirt":
    abc = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//button".format(
        obj['rest.item3'])
    print(abc)
    driver.find_element(By.XPATH, abc).click()
    title3 = driver.find_element(By.XPATH, "//div[@class='inventory_item_label']//div[text()='Sauce Labs Bolt T-Shirt']")
    print(title3.text)
    discription3 = driver.find_element(By.XPATH,
                                       "//div[text()='Sauce Labs Bolt T-Shirt']//ancestor::div[@class='inventory_item_label']//div[@class='inventory_item_desc']")
    print(discription3.text)
    price3 = driver.find_element(By.XPATH,
                                 "//div[text()='Sauce Labs Bolt T-Shirt']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//div")
    print(price3.text)
    time.sleep(3)
elif i == "Sauce Labs Fleece Jacket":
    abc = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//button".format(
        obj['rest.item4'])
    print(abc)
    driver.find_element(By.XPATH, abc).click()
    title4 = driver.find_element(By.XPATH,
                                 "//div[@class='inventory_item_label']//div[text()='Sauce Labs Fleece Jacket']")
    print(title4.text)
    discription4 = driver.find_element(By.XPATH,
                                       "//div[text()='Sauce Labs Fleece Jacket']//ancestor::div[@class='inventory_item_label']//div[@class='inventory_item_desc']")
    print(discription4.text)
    price4 = driver.find_element(By.XPATH,
                                 "//div[text()='Sauce Labs Fleece Jacket']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//div")
    print(price4.text)

    time.sleep(3)

# //div[@class='inventory_item_label']//div[text()='carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.']
#after adding item to the cart
#disrption of item 1 ==//div[text()='Sauce Labs Backpack']//ancestor::div[@class='cart_item_label']//following-sibling::div[@class='inventory_item_desc']
#dis of item2== //div[text()='Sauce Labs Bike Light']//ancestor::div[@class='cart_item_label']//following-sibling::div[@class='inventory_item_desc']
