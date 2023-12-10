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


class TestAddsuccessfully:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_addsuccessfully(self):
        self.driver.get("https://school.moodledemo.net/admin/search.php")
        self.driver.set_window_size(975, 764)
        self.driver.find_element(By.LINK_TEXT, "Users").click()
        self.driver.find_element(By.LINK_TEXT, "Add a new user").click()
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("jomterry")
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(4) > .col-md-9 label"
        ).click()
        self.driver.find_element(By.ID, "id_createpassword").click()
        self.driver.find_element(By.CSS_SELECTOR, "em").click()
        self.driver.find_element(By.ID, "id_firstname").click()
        self.driver.find_element(By.ID, "id_firstname").send_keys("Terry")
        self.driver.find_element(By.ID, "id_lastname").click()
        self.driver.find_element(By.ID, "id_lastname").send_keys("Jom")
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "id_email").send_keys("Terry@Jom.cartoon")
        self.driver.find_element(
            By.CSS_SELECTOR, "#fitem_id_maildisplay > .col-md-9"
        ).click()
        self.driver.find_element(By.ID, "id_submitbutton").click()


class TestMissingUsername:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_missingUsername(self):
        self.driver.get("https://school.moodledemo.net/admin/search.php")
        self.driver.set_window_size(972, 763)
        self.driver.find_element(By.LINK_TEXT, "Users").click()
        self.driver.find_element(By.LINK_TEXT, "Add a new user").click()
        self.driver.find_element(By.ID, "id_firstname").click()
        self.driver.find_element(By.ID, "id_firstname").send_keys("Tom")
        self.driver.find_element(By.ID, "id_lastname").click()
        self.driver.find_element(By.ID, "id_lastname").send_keys("Jerry")
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "id_email").send_keys("Tom@Jerry.cartoon")
        self.driver.find_element(By.ID, "id_submitbutton").click()


class TestWrongEmailaddressformat:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_wrongEmailaddressformat(self):
        self.driver.get("https://school.moodledemo.net/admin/search.php")
        self.driver.set_window_size(974, 764)
        self.driver.find_element(By.LINK_TEXT, "Users").click()
        self.driver.find_element(By.LINK_TEXT, "Add a new user").click()
        self.driver.find_element(By.ID, "id_firstname").click()
        self.driver.find_element(By.ID, "id_firstname").send_keys("Terry")
        self.driver.find_element(By.ID, "id_lastname").click()
        self.driver.find_element(By.ID, "id_lastname").send_keys("Jom")
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "id_email").send_keys("Terry@Jom")
        self.driver.find_element(By.ID, "id_submitbutton").click()
