
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestTest2():
    
    def __init__(self):
      self.setup_method(1)
      self.test_test2()
      self.teardown_method(2)

    def setup_method(self, method):
      self.driver = webdriver.Chrome()
      self.vars = {}
  
    def teardown_method(self, method):
      self.driver.quit()
  
    def test_test2(self):
      self.driver.get("https://bt.rozetka.com.ua/ua/")
      time.sleep(2)
      self.driver.set_window_size(1536, 1024)

      time.sleep(2)
    
      element = self.driver.find_element(By.LINK_TEXT, "Пральні машини")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      time.sleep (2)
      # self.driver.find_element(By.LINK_TEXT, "Пральні машини").click()
      element = WebDriverWait(self.driver, 8).until(
      EC.element_to_be_clickable((By.LINK_TEXT, "Пральні машини"))
      )
      element.click()
      time.sleep(5)

      self.driver.execute_script("window.scrollTo(0,500)")

      element = WebDriverWait(self.driver, 6).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".catalog-grid__cell:nth-child(8) .goods-tile__title"))
            )
      element.click()

      # element = self.driver.find_element(By.CSS_SELECTOR, ".catalog-grid__cell:nth-child(8) .goods-tile__title").click()

      time.sleep(5)

      # self.driver.execute_script("window.scrollTo(0,0)")
      self.driver.find_element(By.CSS_SELECTOR, ".buy-button__label").click()
      self.driver.find_element(By.CSS_SELECTOR, ".cart-footer").click()

      element = self.driver.find_element(By.CSS_SELECTOR, ".cart-footer")
      actions = ActionChains(self.driver)
      actions.double_click(element).perform()
      self.driver.find_element(By.CSS_SELECTOR, ".button_color_gray").click()
      self.driver.find_element(By.CSS_SELECTOR, ".breadcrumbs__item:nth-child(2) > .breadcrumbs__link > span").click()
      element = self.driver.find_element(By.LINK_TEXT, "Кавомашини")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element, 0, 0).perform()
      element = self.driver.find_element(By.LINK_TEXT, "Роботи-пилососи")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element, 0, 0).perform()
      self.driver.find_element(By.CSS_SELECTOR, ".top-widget__categories-item:nth-child(1) .popular-category__title").click()
      element = self.driver.find_element(By.CSS_SELECTOR, ".catalog-grid__cell:nth-child(1) .goods-tile__picture")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element, 0, 0).perform()
      self.driver.execute_script("window.scrollTo(0,404.79998779296875)")
      self.driver.find_element(By.CSS_SELECTOR, ".catalog-grid__cell:nth-child(6) .goods-tile__title").click()
      self.driver.execute_script("window.scrollTo(0,0)")
      self.driver.find_element(By.CSS_SELECTOR, ".button--green > svg").click()
      element = self.driver.find_element(By.CSS_SELECTOR, ".button--green use")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element, 0, 0).perform()
      self.driver.find_element(By.CSS_SELECTOR, ".cart-list__item:nth-child(1) .button:nth-child(3)").click()
      self.driver.find_element(By.CSS_SELECTOR, ".button_size_large > span").click()
      self.driver.execute_script("window.scrollTo(0,0)")
    
my_test = TestTest2()
my_test.test_test2()
