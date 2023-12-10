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
        self.driver.get("https://school.moodledemo.net/my/")
        self.driver.set_window_size(973, 764)
        self.driver.find_element(By.CSS_SELECTOR, ".float-sm-right").click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("SHCD")
        self.driver.find_element(
            By.CSS_SELECTOR, "#fitem_id_eventtype > .col-md-9"
        ).click()
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701753756793_352").click()
        self.driver.find_element(By.ID, "id_duration_2").click()
        self.driver.find_element(By.ID, "id_timedurationminutes").click()
        self.driver.find_element(By.ID, "id_timedurationminutes").send_keys("12")
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701753756793_361").click()
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701753756793_373").click()


class TestBigduration:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_bigduration(self):
        self.driver.get("https://school.moodledemo.net/my/")
        self.driver.set_window_size(972, 763)
        self.driver.find_element(By.CSS_SELECTOR, ".float-sm-right").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".float-sm-right")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".modal-footer > .btn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("SHCD")
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701754409448_348").click()
        self.driver.find_element(By.ID, "id_duration_2").click()
        self.driver.find_element(By.ID, "id_timedurationminutes").click()
        self.driver.find_element(By.ID, "id_timedurationminutes").click()
        self.driver.find_element(By.ID, "id_timedurationminutes").click()
        self.driver.find_element(By.ID, "id_timedurationminutes").send_keys(
            "10000000000000000000"
        )
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701754409448_367").click()


class TestMissingname:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_missingname(self):
        self.driver.get("https://school.moodledemo.net/my/")
        self.driver.set_window_size(975, 764)
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701753902321_67").click()
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701753902321_516").click()


class TestNegativeduration:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_negativeduration(self):
        self.driver.get("https://school.moodledemo.net/my/")
        self.driver.set_window_size(973, 764)
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701754221612_28").click()
        self.driver.execute_script("window.scrollTo(0,1070.4775390625)")
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("SHCD")
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701754221612_525").click()
        self.driver.find_element(By.ID, "id_duration_2").click()
        self.driver.find_element(By.ID, "id_timedurationminutes").click()
        self.driver.find_element(By.ID, "id_timedurationminutes").send_keys("-1")
        self.driver.find_element(By.ID, "yui_3_18_1_1_1701754221612_544").click()
        element = self.driver.find_element(By.ID, "id_duration_0")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
