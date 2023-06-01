import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions
#from Screenshot import Screenshot_clipping
from benedict import benedict
from PIL import Image
#ss = Screenshot.Screenshot_clipping()
options = webdriver.ChromeOptions()

obj = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\ass.yaml")
s1 = obj['rest.browser']
s2 = str.casefold(s1)
browserName = s2
print(browserName)
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "edge":

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("please pass the correct browsername:")
driver.implicitly_wait(10)
driver.get(obj['rest.url'])
# explicit wait
wait = WebDriverWait(driver,10)
element = wait.until(expected_conditions.presence_of_element_located((By.ID,'user-name')))
element.send_keys(obj['rest.user'])
#driver.find_element(By.ID, 'user-name').send_keys(obj['rest.user'])
driver.find_element(By.ID, 'password').send_keys(obj['rest.pass'])
driver.find_element(By.ID, 'login-button').click()
items_list = []
load_data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\ass.yaml")
load_data_items = load_data.get('rest')
for key in load_data_items:
    if 'item' in key:
        print(load_data_items[key])
        items_list.append(load_data_items[key])
print(items_list)
#print(load_data_item1['item1'])
#load_data_item2=load_data.get(obj['rest.item2'])
#print(load_data_item2)
#items_list = [obj['rest.item1'], obj['rest.item2'], obj['rest.item3'], obj['rest.item4']]
#items_list=obj['rest.items']
#list = [obj['rest.item1']]
print(items_list)
#print(obj['rest.item1'][0])

length = len(items_list)
for i in range(length):
    add_button = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']" \
                 "//following-sibling::div[@class='pricebar']//button".format(
        items_list[i])
    print(add_button)
    # explicit wait
    wait = WebDriverWait(driver,10)
    element1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,add_button)))
    element1.click()
    #time.sleep(2)
    #driver.find_element(By.XPATH, add_button).click()
    #print("+++ counting add buttons++++")
    #print(len(driver.find_elements(By.XPATH, "//div[text()='l[i]']//ancestor::div[@class='inventory_item_label']"
                                             #"//following-sibling::div[@class='pricebar']//button")))
    #time.sleep(2)
    title_of_item_shopping_page_1 = "//div[@class='inventory_item_label']//div[text()='{}']".format(items_list[i])
    title_of_item_shopping_page = driver.find_element(By.XPATH, title_of_item_shopping_page_1).text
    print(title_of_item_shopping_page)

    item_description_shopping_page_1 = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']" \
                    "//div[@class='inventory_item_desc']".format(items_list[i])
    item_description_shopping_page = driver.find_element(By.XPATH, item_description_shopping_page_1).text
    print(item_description_shopping_page)
    item_price_shopping_page_1 = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']" \
              "//following-sibling::div[@class='pricebar']//div".format(items_list[i])
    item_price_shopping_page = driver.find_element(By.XPATH, item_price_shopping_page_1).text
    print(item_price_shopping_page)
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(3)
    item_description_cartpage_1 = "//div[text()='{}']//ancestor::div[@class='cart_item_label']" \
                    "//following-sibling::div[@class='inventory_item_desc']".format(items_list[i])
    item_description_cartpage = driver.find_element(By.XPATH, item_description_cartpage_1).text
    print(item_description_cartpage)
    item_price_cart_page_1 = "//div[text()='{}']//ancestor::div[@class='cart_item_label']" \
              "//following-sibling::div[@class='item_pricebar']//div[@class='inventory_item_price']".format(items_list[i])
    item_price_cart_page = driver.find_element(By.XPATH, item_price_cart_page_1).text
    print(item_price_cart_page)
    no_of_item = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/child::a/child::span").text
    print(no_of_item+"  item in cart")
    assert item_description_shopping_page == item_description_cartpage , "validation fail"
    print("validation pass description correct")
    assert item_price_shopping_page == item_price_cart_page, "validation fail"
    print("validation pass price is correct")
    assert title_of_item_shopping_page == items_list[i], "validation fail"
    print("validation pass title is correct")
    #no_of_item=driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']/child::a/child::span").text
    #print(no_of_item)
    #var1=1
    #print(var1)
    #no_of_item1=1
    #assert no_of_item==1,"validation fail"
    #print("validation pass no of item is correct")
    time.sleep(2)
    remove_item = "//div[text()='{}']/parent::a/following-sibling::div[@class='item_pricebar']" \
                "/child::div[@class='inventory_item_price']/following-sibling::button".format(items_list[i])
    removeitem = driver.find_element(By.XPATH,remove_item).click()
    time.sleep(2)
    #driver.find_element(By.XPATH,"//div[@class='cart_footer']/child::button").click()
    after_removing_item_from_cart = driver.find_elements(By.XPATH,"//div[@class='cart_item']"
                                                                  "/child::div[@class='cart_item_label']"
                                                  "/child::a/child::div")
    print(len(after_removing_item_from_cart))
    assert len(after_removing_item_from_cart) == 0,"validation fail"
    print("validation pass no of items in cart is zero")
    driver.find_element(By.XPATH, "//div[@class='cart_footer']/child::button").click()
driver.get_screenshot_as_file('remove.png');
path="C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\name.png"
el = driver.find_element(By.XPATH,'//body')
el.screenshot(path)
driver.quit()

#screen_shot = ss.full_Screenshot(driver, save_path = "C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python", image_name= 'name.png')
#screen = Image.open(screen_shot)
#screen.show()


    # assert title1.text==obj['rest.item2'],"validation fail"
    # print("title is correct")
    # assert price1.text==price2.text,"validation fail"
    # print("price is correct")
    # assert discription.text==discription2.text,"validation fail"
    # print("discription is correct")

    # assert title1.text == obj['rest.item2'], "validationfail"
    # print("pass")

