import pytest
import time 
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestukr():
    def __init__(self):
        self.setup_method(1)
        self.test_testukr()
        self.teardown_method(2)

        
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(10)
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()


    def test_testukr(self):
        self.driver.get("https://www.ukrposhta.ua/ua")
        self.driver.set_window_size(1936, 1168)
        time.sleep(5)
        login_text = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-text"))
        )
        login_text.click()
        self.driver.find_element(By.NAME, "login-user").click()
        time.sleep (2)
        self.driver.find_element(By.NAME, "login-user").click()
        self.driver.find_element(By.LINK_TEXT, "Забули пароль?").click()
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "login").send_keys("prisyazhnyuk1109@gmail.com")
        self.driver.find_element(By.ID, "reset-password").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "identifierId").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "identifierId").send_keys("prisyazhnyuk1109@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        self.driver.find_element(By.NAME, "Passwd").click()
        self.driver.find_element(By.NAME, "Passwd").send_keys("xxxxxxx")
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, ":2d").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "p > a > span").click()
        self.vars["win3300"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win3300"])


my_test = TestTestukr()
my_test.test_testukr()

