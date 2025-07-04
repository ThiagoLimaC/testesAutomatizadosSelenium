# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDelete():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    time.sleep(2)
    self.driver.quit()
  
  def test_delete(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1382, 784)
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .btn-danger > .bi").click()
    time.sleep(2)
    assert self.driver.switch_to.alert.text == "Tem certeza que deseja deletar?"
    time.sleep(2)
    self.driver.switch_to.alert.accept()
  
