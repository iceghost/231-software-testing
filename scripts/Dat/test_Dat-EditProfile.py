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


class TestEditsuccessfully:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_editsuccessfully(self):
        self.driver.get("https://school.moodledemo.net/user/profile.php")
        self.driver.set_window_size(975, 764)
        self.driver.find_element(By.LINK_TEXT, "Edit profile").click()
        self.driver.execute_script("window.scrollTo(0,14.716926574707031)")
        self.driver.execute_script("window.scrollTo(0,269.1599426269531)")
        self.driver.find_element(By.ID, "id_firstname").click()
        self.driver.find_element(By.ID, "id_lastname").click()
        self.driver.find_element(By.ID, "id_lastname").send_keys("Jom")
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "id_email").send_keys("Terr@Jom.cartoon")
        self.driver.find_element(
            By.CSS_SELECTOR, "#fitem_id_moodlenetprofile > .col-md-9"
        ).click()
        self.driver.find_element(By.ID, "id_submitbutton").click()


class TestMissingEmailaddress:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_missingEmailaddress(self):
        self.driver.get("https://school.moodledemo.net/user/profile.php")
        self.driver.set_window_size(972, 763)
        self.driver.find_element(By.LINK_TEXT, "Edit profile").click()
        self.driver.execute_script("window.scrollTo(0,106.59561920166016)")
        self.driver.execute_script("window.scrollTo(0,575.280029296875)")
        self.driver.find_element(By.ID, "id_firstname").click()
        self.driver.find_element(By.CSS_SELECTOR, "#fitem_id_email > .col-md-9").click()
        self.driver.find_element(By.ID, "id_lastname").click()
        self.driver.find_element(By.ID, "id_lastname").send_keys("Jom")
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701749554810_463").click()
        self.driver.find_element(By.ID, "id_submitbutton").click()


class TestMissingFirstname:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_missingFirstname(self):
        self.driver.get("https://school.moodledemo.net/user/profile.php")
        self.driver.set_window_size(972, 763)
        self.driver.find_element(By.LINK_TEXT, "Edit profile").click()
        self.driver.find_element(By.ID, "id_firstname").click()
        self.driver.find_element(By.ID, "id_firstname").click()
        element = self.driver.find_element(By.ID, "id_firstname")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(
            By.CSS_SELECTOR, "#fitem_id_imagealt > .col-md-9"
        ).click()
        self.driver.find_element(By.ID, "id_submitbutton").click()


class TestMissngLastname:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_missngLastname(self):
        self.driver.get("https://school.moodledemo.net/user/profile.php")
        self.driver.set_window_size(972, 763)
        self.driver.find_element(By.LINK_TEXT, "Edit profile").click()
        self.driver.find_element(By.ID, "id_firstname").click()
        self.driver.find_element(By.ID, "id_firstname").click()
        element = self.driver.find_element(By.ID, "id_firstname")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "id_firstname").send_keys("Terry")
        self.driver.find_element(By.ID, "id_moodlecontainer").click()
        self.driver.find_element(By.ID, "id_lastname").click()
        self.driver.find_element(By.ID, "id_lastname").click()
        element = self.driver.find_element(By.ID, "id_lastname")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        element = self.driver.find_element(
            By.CSS_SELECTOR, "#fitem_id_maildisplay > .col-md-9"
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "id_moodlecontainer")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "id_moodlecontainer").click()
        self.driver.find_element(By.ID, "id_submitbutton").click()


class TestWrongEmailaddressformat:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_wrongEmailaddressformat(self):
        self.driver.get("https://school.moodledemo.net/user/profile.php")
        self.driver.set_window_size(972, 763)
        self.driver.find_element(By.LINK_TEXT, "Edit profile").click()
        self.driver.find_element(By.ID, "id_firstname").click()
        self.driver.find_element(By.ID, "id_lastname").click()
        self.driver.find_element(By.ID, "id_lastname").send_keys("Jom")
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "id_email").send_keys("Terry@Jom")
        self.driver.find_element(
            By.CSS_SELECTOR, "#fitem_id_moodlenetprofile > .col-md-9"
        ).click()
        self.driver.find_element(By.ID, "id_submitbutton").click()
