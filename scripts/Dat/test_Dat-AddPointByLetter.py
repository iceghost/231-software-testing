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


class TestAddwithoutletter:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_addwithoutletter(self):
        self.driver.get(
            "https://school.moodledemo.net/grade/edit/letter/index.php?id=269"
        )
        self.driver.set_window_size(972, 764)
        self.driver.find_element(By.ID, "single_button656e8fed72b4c28").click()
        self.driver.find_element(By.ID, "id_gradeentryadd").click()
        self.driver.find_element(By.ID, "id_gradeboundary_10").click()
        self.driver.find_element(By.ID, "id_gradeboundary_10").send_keys("50")
        self.driver.find_element(By.ID, "id_submitbutton").click()


class TestInputwrongtypeofpoint:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_inputwrongtypeofpoint(self):
        self.driver.get(
            "https://school.moodledemo.net/grade/edit/letter/index.php?id=269"
        )
        self.driver.set_window_size(972, 763)
        self.driver.find_element(By.ID, "single_button656e93a2973aa28").click()
        self.driver.find_element(By.ID, "id_gradeentryadd").click()
        self.driver.execute_script("window.scrollTo(0,42.95832443237305)")
        self.driver.find_element(By.ID, "id_gradeletter_11").click()
        self.driver.find_element(By.ID, "id_gradeletter_11").send_keys("A")
        self.driver.find_element(By.ID, "id_gradeboundary_11").click()
        self.driver.find_element(By.ID, "id_gradeboundary_11").send_keys("50ss")
        self.driver.find_element(
            By.CSS_SELECTOR, "#fitem_id_gradeentryadd > .col-md-9"
        ).click()
        self.driver.find_element(By.ID, "id_submitbutton").click()


class TestInputwrongtypeofpoint2:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_inputwrongtypeofpoint2(self):
        self.driver.get(
            "https://school.moodledemo.net/grade/edit/letter/index.php?id=269"
        )
        self.driver.set_window_size(972, 764)
        self.driver.find_element(By.ID, "single_button656e94012317028").click()
        self.driver.find_element(By.ID, "id_gradeentryadd").click()
        self.driver.find_element(By.ID, "id_gradeletter_11").click()
        self.driver.find_element(By.ID, "id_gradeletter_11").send_keys("A")
        self.driver.find_element(By.ID, "id_gradeboundary_11").click()
        self.driver.find_element(By.ID, "id_gradeboundary_11").send_keys("50abc")
        self.driver.find_element(By.ID, "id_submitbutton").click()
