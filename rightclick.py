from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
logging.basicConfig(filename="loggg.log",filemode="w",level=logging.DEBUG,format='%(asctime)s %(message)s',)


# Test messages
logging.debug("Harmless debug Message")
logging.info("Just an information")
logging.warning("Its a Warning")
logging.error("Did you try to divide by zero")
logging.critical("Internet is down")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
#right link/context click
right_ele = driver.find_element(By.XPATH,"//span[text()='right click me']")
act_chain = ActionChains(driver)
time.sleep(3)
act_chain.context_click(right_ele).perform()
driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-edit']").click()
time.sleep(3)
logging.info("done")