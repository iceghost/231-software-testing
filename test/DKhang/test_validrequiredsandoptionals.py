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

class TestValidrequiredsandoptionals():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_validrequiredsandoptionals(self):
    self.driver.get("https://sandbox.moodledemo.net/")
    self.driver.set_window_size(1850, 1048)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.ID, "password").send_keys("sandbox")
    self.driver.find_element(By.ID, "loginbtn").click()
    self.driver.find_element(By.LINK_TEXT, "Site administration").click()
    self.driver.find_element(By.LINK_TEXT, "Users").click()
    self.driver.find_element(By.LINK_TEXT, "Add a new user").click()
    self.driver.find_element(By.ID, "id_username").send_keys("khangng")
    self.driver.find_element(By.CSS_SELECTOR, "em").click()
    self.driver.find_element(By.ID, "id_newpassword").send_keys("12345678")
    self.driver.find_element(By.ID, "id_firstname").send_keys("Khang")
    self.driver.find_element(By.ID, "id_lastname").send_keys("Nguyen")
    self.driver.find_element(By.ID, "id_email").send_keys("khangng@gmail.com")
    self.driver.find_element(By.ID, "id_moodlenetprofile").send_keys("khangng")
    self.driver.find_element(By.ID, "id_city").send_keys("HCM")
    self.driver.find_element(By.ID, "id_submitbutton").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, "div.alert.alert-success")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "id_realname").send_keys("khang nguyen")
    self.driver.find_element(By.ID, "id_realname").send_keys(Keys.ENTER)
    self.driver.find_element(By.XPATH, "//td[6]/a/i").click()
    self.driver.find_element(By.XPATH, "//div[2]/form/button").click()
    self.driver.find_element(By.ID, "user-menu-toggle").click()
    self.driver.find_element(By.LINK_TEXT, "Log out").click()
  
