from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
time.sleep(5)
driver.find_element(By.ID,'newWindowBtn').click()
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    driver.maximize_window()
time.sleep(5)
#driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys('divakar')
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys('reddy')
driver.find_element(By.ID,'femalerb').click()
driver.find_element(By.ID,'spanishchbx').click()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('divakar2000@gmail')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('password')