#adding 4 items to card
#dynamically picking items from yaml file
#adding one item and removing one item and doing assertion
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions


def test_3():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.support import expected_conditions
    # from Screenshot import Screenshot_clipping
    from benedict import benedict
    from PIL import Image
    # ss = Screenshot.Screenshot_clipping()
    options = webdriver.ChromeOptions()

    obj = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\ass.yaml")
    s1 = obj['rest.browser']
    s2 = str.casefold(s1)
    browserName = s2
    print(browserName)
    if browserName == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browserName == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browserName == "edge":

        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        print("please pass the correct browsername:")
    driver.implicitly_wait(10)
    driver.get(obj['rest.url'])
    # explicit wait
    wait = WebDriverWait(driver, 10)
    element = wait.until(expected_conditions.presence_of_element_located((By.ID, 'user-name')))
    element.send_keys(obj['rest.user'])
    # driver.find_element(By.ID, 'user-name').send_keys(obj['rest.user'])
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
    # print(load_data_item1['item1'])
    # load_data_item2=load_data.get(obj['rest.item2'])
    # print(load_data_item2)
    # items_list = [obj['rest.item1'], obj['rest.item2'], obj['rest.item3'], obj['rest.item4']]
    # items_list=obj['rest.items']
    # list = [obj['rest.item1']]
    print(items_list)
    # print(obj['rest.item1'][0])

    length = len(items_list)
    for i in range(length):
        add_button = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']" \
                     "//following-sibling::div[@class='pricebar']//button".format(
            items_list[i])
        print(add_button)
        # explicit wait
        wait = WebDriverWait(driver, 10)
        element1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, add_button)))
        element1.click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, add_button).click()
        # print("+++ counting add buttons++++")
        # print(len(driver.find_elements(By.XPATH, "//div[text()='l[i]']//ancestor::div[@class='inventory_item_label']"
        # "//following-sibling::div[@class='pricebar']//button")))
        # time.sleep(2)
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
                                 "//following-sibling::div[@class='item_pricebar']//div[@class='inventory_item_price']".format(
            items_list[i])
        item_price_cart_page = driver.find_element(By.XPATH, item_price_cart_page_1).text
        print(item_price_cart_page)
        no_of_item = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/child::a/child::span").text
        print(no_of_item + "  item in cart")
        assert item_description_shopping_page == item_description_cartpage, "validation fail"
        print("validation pass description correct")
        assert item_price_shopping_page == item_price_cart_page, "validation fail"
        print("validation pass price is correct")
        assert title_of_item_shopping_page == items_list[i], "validation fail"
        print("validation pass title is correct")
        # no_of_item=driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']/child::a/child::span").text
        # print(no_of_item)
        # var1=1
        # print(var1)
        # no_of_item1=1
        # assert no_of_item==1,"validation fail"
        # print("validation pass no of item is correct")
        time.sleep(2)
        remove_item = "//div[text()='{}']/parent::a/following-sibling::div[@class='item_pricebar']" \
                      "/child::div[@class='inventory_item_price']/following-sibling::button".format(items_list[i])
        removeitem = driver.find_element(By.XPATH, remove_item).click()
        time.sleep(2)
        # driver.find_element(By.XPATH,"//div[@class='cart_footer']/child::button").click()
        after_removing_item_from_cart = driver.find_elements(By.XPATH, "//div[@class='cart_item']"
                                                                       "/child::div[@class='cart_item_label']"
                                                                       "/child::a/child::div")
        print(len(after_removing_item_from_cart))
        assert len(after_removing_item_from_cart) == 0, "validation fail"
        print("validation pass no of items in cart is zero")
        driver.find_element(By.XPATH, "//div[@class='cart_footer']/child::button").click()
    driver.get_screenshot_as_file('remove.png');
    path = "C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\name.png"
    el = driver.find_element(By.XPATH, '//body')
    el.screenshot(path)
    driver.quit()

#adding 6 items to cart and remove 6 items and doing assertion
#selecting filter and doing assertion for filter
def test_4():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.ui import Select
    from benedict import benedict

    obj = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\assignment4.yaml")
    s1 = obj['rest.browser']
    s2 = str.casefold(s1)
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
    # explicit wait
    wait = WebDriverWait(driver, 10)
    element = wait.until(expected_conditions.presence_of_element_located((By.ID, 'user-name')))
    element.send_keys(obj['rest.user'])
    # driver.find_element(By.ID, 'user-name').send_keys(obj['rest.user'])
    driver.find_element(By.ID, 'password').send_keys(obj['rest.pass'])
    driver.find_element(By.ID, 'login-button').click()
    # for select class assertion
    total_1 = driver.find_elements(By.XPATH, "//div[@class='inventory_container']/div/div")
    list1 = []
    for i in total_1:
        # print(i.text)
        list1.append(i.text)
    print(list1)

    items_list = [obj['rest.item1'], obj['rest.item2'], obj['rest.item3'], obj['rest.item4'], obj['rest.item5'],
                  obj['rest.item6']]
    print(items_list)
    length = len(items_list)
    for i in range(length):
        add_button = "//div[text()='{}']//ancestor::div[@class='inventory_item_label']" \
                     "//following-sibling::div[@class='pricebar']//button".format(
            items_list[i])
        wait = WebDriverWait(driver, 10)
        element1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, add_button)))
        element1.click()
        time.sleep(2)
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
        driver.find_element(By.XPATH,
                            "//div[@class='shopping_cart_container']/child::a[@class='shopping_cart_link']").click()
        item_description_cartpage_1 = "//div[text()='{}']//ancestor::div[@class='cart_item_label']" \
                                      "//following-sibling::div[@class='inventory_item_desc']".format(items_list[i])
        item_description_cartpage = driver.find_element(By.XPATH, item_description_cartpage_1).text
        print(item_description_cartpage)
        item_price_cart_page_1 = "//div[text()='{}']//ancestor::div[@class='cart_item_label']" \
                                 "//following-sibling::div[@class='item_pricebar']//div[@class='inventory_item_price']".format(
            items_list[i])
        item_price_cart_page = driver.find_element(By.XPATH, item_price_cart_page_1).text
        print(item_price_cart_page)
        time.sleep(2)
        # driver.find_element(By.XPATH,"//div[@class='cart_footer']/child::button").click()
        driver.find_element(By.XPATH, "//div[@class='cart_footer']/child::button").click()
        time.sleep(2)
        assert item_description_shopping_page == item_description_cartpage, "validation fail"
        print("validation pass description correct")
        assert item_price_shopping_page == item_price_cart_page, "validation fail"
        print("validation pass price is correct")
        assert title_of_item_shopping_page == items_list[i], "validation fail"
        print("validation pass title is correct")
        # driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
        # driver.find_element(By.XPATH,"//div[@class='shopping_cart_container']/child::a").click()
        # time.sleep(3)
        # remove_item = "//div[text()='{}']/parent::a/following-sibling::div[@class='item_pricebar']" \
        # "/child::div[@class='inventory_item_price']/following-sibling::button".format(items_list[i])
        # removeitem = driver.find_element(By.XPATH, remove_item).click()
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(3)
    for i in range(length):
        # remove_item = "//button[@id='remove-{}']".format(items_list[i])
        remove_item = "//div[text()='{}']/parent::a/following-sibling::div[@class='item_pricebar']" \
                      "/child::div[@class='inventory_item_price']/following-sibling::button".format(items_list[i])
        removeitem = driver.find_element(By.XPATH, remove_item).click()
        # remove_item_text=driver.find_element(By.XPATH,remove_item).text
        # print(remove_item_text)
        time.sleep(3)
        assert_item = "//div[@class='cart_item_label']/child::a/child::div[text()='{}']".format(items_list[i])
        assert_items = driver.find_elements(By.XPATH, assert_item)
        print(len(assert_items))
        assert len(assert_items) == 0, "validation fail"
        print(items_list[i] + '  is removed')
        after_removing_item_from_cart = driver.find_elements(By.XPATH, "//div[@class='cart_item']"
                                                                       "/child::div[@class='cart_item_label']"
                                                                       "/child::a/child::div")
        # driver.find_element(By.XPATH,"//button[@class='btn btn_secondary back btn_medium']").click()

    print(len(after_removing_item_from_cart))
    assert len(after_removing_item_from_cart) == 0, "validation fail"
    print("validation pass no of items in cart is zero")
    driver.find_element(By.XPATH, "//div[@class='cart_footer']/child::button").click()

    time.sleep(3)
    drop_down = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    drp = Select(drop_down)
    # drp.select_by_visible_text('Name (Z to A)')
    time.sleep(3)
    # drp.select_by_index(1)
    # time.sleep(2)
    drp.select_by_value('za')
    time.sleep(2)
    total = driver.find_elements(By.XPATH, "//div[@class='inventory_container']/div/div")
    list2 = []
    for i in total:
        # print(i.text)
        list2.append(i.text)
    list2.reverse()
    print(list2)
    assert list1 == list2, "validation fail"
    print("dropdown box selected successfully")
    driver.quit()

#pop-up message alert message
#alert.accept()
#alert.dismiss()
#alert.sendkeys()

def test_alert():
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.wait import WebDriverWait
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://the-internet.herokuapp.com/javascript_alerts")
    # wait = WebDriverWait(driver,10)
    # element1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='Click for JS Alert']")))
    # element1.click()
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    time.sleep(3)
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    ele = driver.switch_to.alert
    print(ele.text)
    ele.accept()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    ele2 = driver.switch_to.alert
    time.sleep(4)
    ele2.send_keys('divi')
    ele2.accept()
    # print(ele2.text)
    # ele2.dismiss()
    time.sleep(3)

#popup messages
#windows handling

def test_alert1():
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
    driver.execute_script("window.scrollTo(0,200);")
    time.sleep(5.0)
    driver.find_element(By.XPATH, "//button[@id='newWindowBtn']").click()
    time.sleep(5.0)
    driver.find_element(By.XPATH, "//button[@id='newTabBtn']").click()
    time.sleep(10)
    # windows handle
    print(driver.current_window_handle)  # -parent
    handles = driver.window_handles  # return all the handle values of opened browser window
    for handle in handles:
        driver.switch_to.window(handle)
        print(driver.title)
    driver.find_element(By.XPATH, "//button[@id='alertBox']").click()

    alert = driver.switch_to.alert
    # print(alert.text)
    alert.accept()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@onclick='confirmFunction()']").click()
    alert1 = driver.switch_to.alert
    alert1.accept()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@onclick='promptFunction()']").click()
    alert2 = driver.switch_to.alert
    alert2.send_keys("divakar reddy")
    alert2.accept()
    time.sleep(5)
    driver.quit()


