import logging
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
    logging.debug('The debug message is displaying')
    logging.info('The info message is displaying')
    time.sleep(5)
    # if we want to drag and drop by cordinates
    # actions.drag_and_drop_by_offset(ele1,40,50).perform()
    time.sleep(5)



