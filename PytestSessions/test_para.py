from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
import time

driver = None
firstname="Divakar"
lastname="reddy"
email="divakar@gmail.com"
password="123456"


def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)



def teardown_module(module):
    driver.quit()


'''@pytest.mark.parametrize(
                            "firstname","lastname","email","password",
                             [
                                ("divi","reddy","divi2000@gmail","divi123"),
                                ("raj","reddy","raju200@gmail.com","raj123"),
                             ]
                        )'''


def test_login():
    driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
    driver.execute_script("window.scrollTo(0,200);")
    action=Action
    time.sleep(5.0)
    driver.find_element(By.ID, 'newWindowBtn').click()
    handles = driver.window_handles
    for handle in handles:
        driver.switch_to.window(handle)
        print(driver.title)
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(firstname)
    driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(lastname)
    driver.find_element(By.ID,'femalerb').click()
    driver.find_element(By.ID,'spanishchbx').click()
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

