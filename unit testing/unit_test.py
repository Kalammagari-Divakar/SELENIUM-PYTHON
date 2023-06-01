import unittest
import time
from add import add
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
#driver=None


class UnitTesting(unittest.TestCase):

    def setUp(self):
        #global driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("end")

    def test_keyboard_operations(self):
        self.driver.get("https://www.thetestingworld.com/testings/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "fld_username").send_keys("Divakar reddy")
        actions = ActionChains(self.driver)
        '''actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CON
        actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()'''
        actions.send_keys(Keys.TAB).perform()
        self.driver.find_element(By.NAME, "fld_email").send_keys("kdivakar2000@gmail.com")
        actions.send_keys(Keys.TAB).perform()
        self.driver.find_element(By.NAME, "fld_password").send_keys("divi@20")
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        actions.send_keys(Keys.TAB)
        actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        actions.send_keys(Keys.TAB).perform()
        self.driver.find_element(By.ID, "datepicker").click()
        self.driver.find_element(By.XPATH, "//a[text()='19']").click()
        actions.send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, 'phone').send_keys("+918523476456")
        actions.send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "address").send_keys("e-city,bangalore")
        self.driver.find_element(By.XPATH, "//input[@value='office']").click()
        ele1 = self.driver.find_element(By.NAME, 'sex')
        drp1 = Select(ele1)
        time.sleep(2)
        drp1.select_by_index(1)
        ele2 = self.driver.find_element(By.NAME, "country")
        drp2 = Select(ele2)
        drp2.select_by_visible_text('India')
        ele3 = self.driver.find_element(By.ID, "stateId")
        drp3 = Select(ele3)
        self.driver.implicitly_wait(10)
        drp3.select_by_visible_text("Andhra Pradesh")
        ele4 =self.driver.find_element(By.ID, "cityId")
        drp4 = Select(ele4)
        self.driver.implicitly_wait(10)
        drp4.select_by_visible_text("Chittoor")
        self.driver.find_element(By.NAME, "zip").send_keys("517247")
        self.driver.find_element(By.NAME, "terms").click()
        self.driver.find_element(By.XPATH, "//input[@value='Sign up']").click()
        time.sleep(5)

    def test_mouse_operations(self):
        self.driver.get("https://www.thetestingworld.com/#")
        actions = ActionChains(self.driver)
        # moving mouse to particular place

        actions.move_to_element(self.driver.find_element(By.ID, "menu576")).perform()
        # left click of mouse
        actions.click().perform()
        # right click of mouse
        actions.context_click().perform()
        # click at a specific point
        actions.click(self.driver.find_element(By.XPATH, "//a[text()='Quick Demo']")).perform()
        # right click at a specific point
        # actions.context_click(driver.find_element(By.ID,"wdform_1_element_first2")).perform()
        # double click
        actions.double_click().perform()
        # double click at specific location
        actions.double_click(self.driver.find_element(By.XPATH, "//button[text()='Submit']")).perform()
        time.sleep(10)
    def test_add(self):
        print(add(10,20.0))



if __name__ == '__main__':
    unittest.main()


