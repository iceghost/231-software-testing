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


class TestAddUser:
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.get("https://sandbox.moodledemo.net/")
        self.driver.set_window_size(1850, 1048)
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("sandbox")
        self.driver.find_element(By.ID, "loginbtn").click()
        self.driver.find_element(By.LINK_TEXT, "Site administration").click()
        self.driver.find_element(By.LINK_TEXT, "Users").click()
        self.driver.find_element(By.LINK_TEXT, "Add a new user").click()

    def teardown_method(self, method):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.driver.close()


class TestAddUserValid(TestAddUser):
    def teardown_method(self, method):
        self.driver.find_element(By.ID, "id_realname").send_keys("khang nguyen")
        self.driver.find_element(By.ID, "id_realname").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//td[6]/a/i").click()
        self.driver.find_element(By.XPATH, "//div[2]/form/button").click()
        super().setup_method(method)

    @pytest.mark.parametrize("extra", [False, True], ids=["without optional fields", "with optional fields"])
    def test_valid(self, extra):
        self.driver.find_element(By.ID, "id_username").send_keys("khangng")
        self.driver.find_element(By.CSS_SELECTOR, "em").click()
        self.driver.find_element(By.ID, "id_newpassword").send_keys("12345678")
        self.driver.find_element(By.ID, "id_firstname").send_keys("Khang")
        self.driver.find_element(By.ID, "id_lastname").send_keys("Nguyen")
        self.driver.find_element(By.ID, "id_email").send_keys("khangng@gmail.com")
        if extra:
            self.driver.find_element(By.ID, "id_moodlenetprofile").send_keys("khangng")
            self.driver.find_element(By.ID, "id_city").send_keys("HCM")
        self.driver.find_element(By.ID, "id_submitbutton").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.alert.alert-success")
        assert len(elements) > 0


class TestAddUserInvalid(TestAddUser):
    @pytest.mark.parametrize(
        "username,email,lastname",
        [
            ("khangng", "khangng@", "Nguyen"),
            ("siu!@$!@$!@$", "khangng@gmail.com", "Nguyen"),
            ("khangng", "khangng@gmail.com", ""),
        ],
        ids=["invalid email", "invalid username", "missing lastname"]
    )
    def test_invalid(self, username, email, lastname):
        self.driver.find_element(By.ID, "id_username").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "em").click()
        self.driver.find_element(By.ID, "id_newpassword").send_keys("12345678")
        self.driver.find_element(By.ID, "id_firstname").send_keys("Khang")
        self.driver.find_element(By.ID, "id_lastname").send_keys(lastname)
        self.driver.find_element(By.ID, "id_email").send_keys(email)
        self.driver.find_element(By.ID, "id_submitbutton").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.invalid-feedback")
        assert len(elements) > 0
