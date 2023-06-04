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

class TestMakeAppointmentHeroku():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_makeAppointmentHeroku(self):
    self.driver.get("https://katalon-demo-cura.herokuapp.com/")
    self.driver.set_window_size(1552, 880)
    self.driver.find_element(By.ID, "txt_visit_date").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > .day:nth-child(5)").click()
    self.driver.find_element(By.ID, "txt_comment").click()
    self.driver.find_element(By.ID, "txt_comment").send_keys("booking")
    self.driver.find_element(By.ID, "chk_hospotal_readmission").click()
    self.driver.find_element(By.ID, "btn-book-appointment").click()
  
