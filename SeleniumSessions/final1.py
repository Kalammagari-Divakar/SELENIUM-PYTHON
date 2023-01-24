import time
import logging
from selenium import webdriver
from selenium.webdriver.common import keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from benedict import benedict

driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.implicitly_wait(10)


def teardown_module(module):
    driver.quit()

    # adding 4 items to card
    # dynamically picking items from yaml file
    # adding one item and removing one item and doing assertion


def test_3():
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

    # adding 6 items to cart and remove 6 items and doing assertion
    # selecting filter and doing assertion for filter


def test_4():
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
    # driver.quit()

    # pop-up message alert message
    # alert.accept()
    # alert.dismiss()
    # alert.sendkeys()


def test_alert():
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

    # popup messages
    # windows handling


def test_alert1():
    # from selenium import webdriver
    # import time
    # from selenium.webdriver.common.by import By
    # from webdriver_manager.chrome import ChromeDriverManager

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
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.ID, 'alertBox').click()

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
    # driver.quit()


def test_keyboard_operations():
    # from selenium import webdriver
    # import time
    # from webdriver_manager.chrome import ChromeDriverManager
    # from selenium.webdriver.support.ui import Select
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.common.keys import Keys
    # from selenium.webdriver.common.action_chains import ActionChains
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.thetestingworld.com/testings/")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "fld_username").send_keys("Divakar reddy")
    actions = ActionChains(driver)
    '''actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CON
    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()'''
    actions.send_keys(Keys.TAB).perform()
    driver.find_element(By.NAME, "fld_email").send_keys("kdivakar2000@gmail.com")
    actions.send_keys(Keys.TAB).perform()
    driver.find_element(By.NAME, "fld_password").send_keys("divi@20")
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.TAB)
    actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.TAB).perform()
    driver.find_element(By.ID, "datepicker").click()
    driver.find_element(By.XPATH, "//a[text()='19']").click()
    actions.send_keys(Keys.TAB)
    driver.find_element(By.NAME, 'phone').send_keys("+918523476456")
    actions.send_keys(Keys.TAB)
    driver.find_element(By.NAME, "address").send_keys("e-city,bangalore")
    driver.find_element(By.XPATH, "//input[@value='office']").click()
    ele1 = driver.find_element(By.NAME, 'sex')
    drp1 = Select(ele1)
    time.sleep(2)
    drp1.select_by_index(1)
    ele2 = driver.find_element(By.NAME, "country")
    drp2 = Select(ele2)
    drp2.select_by_visible_text('India')
    ele3 = driver.find_element(By.ID, "stateId")
    drp3 = Select(ele3)
    driver.implicitly_wait(10)
    drp3.select_by_visible_text("Andhra Pradesh")
    ele4 = driver.find_element(By.ID, "cityId")
    drp4 = Select(ele4)
    driver.implicitly_wait(10)
    drp4.select_by_visible_text("Chittoor")
    driver.find_element(By.NAME, "zip").send_keys("517247")
    driver.find_element(By.NAME, "terms").click()
    driver.find_element(By.XPATH, "//input[@value='Sign up']").click()
    time.sleep(5)


def test_mouse_operations():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.thetestingworld.com/#")
    actions = ActionChains(driver)
    # moving mouse to particular place

    actions.move_to_element(driver.find_element(By.ID, "menu576")).perform()
    # left click of mouse
    actions.click().perform()
    # right click of mouse
    actions.context_click().perform()
    # click at a specific point
    actions.click(driver.find_element(By.XPATH, "//a[text()='Quick Demo']")).perform()
    # right click at a specific point
    # actions.context_click(driver.find_element(By.ID,"wdform_1_element_first2")).perform()
    # double click
    actions.double_click().perform()
    # double click at specific location
    actions.double_click(driver.find_element(By.XPATH, "//button[text()='Submit']")).perform()
    time.sleep(10)


def test_scrolling():
    data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\insta.yaml")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(data['test_scrolling.url'])
    driver.maximize_window()
    time.sleep(10)
    # scrolling window with pixel size
    # driver.execute_script("window.scrollBy(0,1000)","")
    # time.sleep(5)
    # scrolling down a page till the element is visible
    flag = driver.find_element(By.XPATH, data['test_scrolling.element'])
    driver.execute_script("arguments[0].scrollIntoView(true);", flag)
    time.sleep(5)
    # scroll down till end
    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


# iframes

def test_iframes():
    data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\insta.yaml")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(data['test_iframes.url'])
    driver.maximize_window()
    driver.switch_to.frame(data['test_iframes.first frame'])  # first frame
    driver.find_element(By.LINK_TEXT, data['test_iframes.click in first frame']).click()
    driver.switch_to.default_content()
    driver.switch_to.frame(data['test_iframes.second frame'])  # second frame
    driver.find_element(By.LINK_TEXT, data['test_iframes.click in second frame']).click()
    driver.switch_to.default_content()
    driver.switch_to.frame(data['test_iframes.third frame'])  # third frame
    driver.find_element(By.LINK_TEXT, data['test_iframes.click in third frame']).click()
    # driver.find_element_by_link_text("org.openqa.selenium").click()
    time.sleep(5)


def test_iframe1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    driver.maximize_window()
    driver.switch_to.frame("google_esf")
    driver.switch_to.default_content()
    driver.switch_to.frame("globalSqa")
    actions = ActionChains(driver)
    # moving mouse to particular place

    actions.move_to_element(driver.find_element(By.XPATH, "//div//span[@id='current_filter']")).perform()
    driver.find_element(By.XPATH, "//li/div[text()='Software Testing']").click()
    time.sleep(5)


def test_window_handles():
    data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\insta.yaml")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(data['window_handles.url'])
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0,900)")
    time.sleep(5)
    # click id
    driver.find_element(By.ID, data['window_handles.id']).click()
    time.sleep(5)
    print(driver.current_window_handle)
    handles = driver.window_handles
    print(handles)
    for handle in handles:
        driver.switch_to.window(handle)
        print(driver.title)
    frst_child = driver.window_handles[0]  # withe the help of index we will switch to differnt windows
    # to switch focus the first child window handle
    driver.switch_to.window(frst_child)
    time.sleep(5)


# Python Selenium is_displayed(), is_enabled() and is_selected() Methods

def test_is_displayed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\insta.yaml")
    driver.get(data['is_displayed.url'])
    time.sleep(3)
    # username
    user_name = driver.find_element(By.XPATH, data['is_displayed.username'])
    print(user_name.is_displayed(), 'user coloumn is displayed or not')
    if user_name.is_displayed() == True:
        driver.find_element(By.NAME, "username").send_keys(data['is_displayed.username keys'])
        time.sleep(5)
    pswrd = driver.find_element(By.NAME, "password")
    print(pswrd.is_displayed(), 'password coloumn is displayed or not')
    if pswrd.is_displayed() == True:
        driver.find_element(By.NAME, "password").send_keys(data['is_displayed.password keys'])
        time.sleep(5)
    login = driver.find_element(By.XPATH, data['is_displayed.login'])
    print(login.is_enabled(), 'login button is enable or not')
    if login.is_enabled() == True:
        driver.find_element(By.XPATH, data['is_displayed.login']).click()
        time.sleep(5)
    # is selected
    driver.get(data['is_displayed.isselected.url'])
    select = driver.find_element(By.XPATH, data['is_displayed.isselected.select'])
    print(select.is_selected(), 'check box is selected or not')
    select1 = driver.find_element(By.XPATH, data['is_displayed.isselected.select1'])
    print(select1.is_selected(), 'check box is selected or not')
    time.sleep(10)
    # is enable
    driver.get(data['is_displayed.isenable.url'])
    enable = driver.find_element(By.ID, data['is_displayed.isenable.enable'])
    time.sleep(5)
    print(enable.is_enabled(), 'button is enable or not ')


# Selenium Python Tutorial - How to Get Element Attribute Value

def test_get_attribute():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\insta.yaml")
    driver.get(data['hrm.url'])
    driver.find_element(By.NAME, "username").send_keys(data['hrm.username'])
    driver.find_element(By.NAME, "password").send_keys(data['hrm.password'])
    attribute = driver.find_element(By.XPATH, "//button[text()=' Login ']").get_attribute("type")
    time.sleep(10)
    print(attribute, "is the attribute value")
    if attribute == 'submit':
        driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        time.sleep(3)


def test_screenshot():
    data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\insta.yaml")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(data['screenshot.url'])
    time.sleep(3)
    login = driver.find_element(By.XPATH, data['screenshot.login_button'])
    # capture the screenshot of a particular elemnet with xpath
    login.screenshot("C:\\Users\\uif48567\\Pictures\\Saved Pictures\\image.png")
    # username
    driver.find_element(By.NAME, data['screenshot.username']).send_keys('12355')
    # pswrd
    driver.find_element(By.NAME, data['screenshot.password']).send_keys('12331200')
    # login
    driver.find_element(By.XPATH, data['screenshot.login']).click()
    time.sleep(2)
    driver.get_screenshot_as_file("C:\\Users\\uif48567\\Pictures\\Saved Pictures\\image1.png")
    driver.save_screenshot("C:\\Users\\uif48567\\Pictures\\Saved Pictures\\image2.png")


# Selenium Python  - How to handle Auto Suggestion in Selenium

def test_auto_suggestions():
    data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\insta.yaml")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(data['autosuggestions.url'])
    # importing module
    import logging

    driver.maximize_window()
    depart_from = driver.find_element(By.NAME, data['autosuggestions.depart_from'])
    depart_from.click()
    time.sleep(2)
    depart_from.send_keys("New")
    time.sleep(2)
    depart_from.send_keys(Keys.ENTER)
    time.sleep(10)
    going_to = driver.find_element(By.NAME, data['autosuggestions.going_to'])
    going_to.send_keys("New")
    time.sleep(3)
    suggestions = driver.find_elements(By.XPATH, data['autosuggestions.suggestions'])
    print(len(suggestions))
    for i in suggestions:
        print(i.text)
        if "New York (JFK)" in i.text:
            i.click()
            time.sleep(3)
            break

    # Selenium Python - How to handle Calendar in Selenium
    time.sleep(5)
    driver.find_element(By.XPATH, data['autosuggestions.date']).click()
    time.sleep(5)
    all_dates = driver.find_elements(By.XPATH, data['autosuggestions.all_dates'])

    for dates in all_dates:
        if "24/02/2023" in dates.get_attribute("data-date"):
            dates.click()
            time.sleep(5)

            break
    driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
    time.sleep(5)
    # logging.info("passed it successfully")


# Selenium Python Tutorial #39 - How to Perform Drag and Drop in Selenium

def test_drag_drop():
    data = benedict.from_yaml("C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\insta.yaml")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(data['drag_drop.url'])
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, data['drag_drop.switchto']))
    ele1 = driver.find_element(By.ID, data['drag_drop.element1'])
    ele2 = driver.find_element(By.ID, data['drag_drop.element2'])
    actions = ActionChains(driver)
    actions.drag_and_drop(ele1, ele2).perform()
    time.sleep(5)
    # if we want to drag and drop by cordinates
    # actions.drag_and_drop_by_offset(ele1,40,50).perform()
    time.sleep(5)
