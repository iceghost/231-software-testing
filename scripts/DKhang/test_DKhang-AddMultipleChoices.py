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

TEXTS = [
    "Functionalities of software applications are tested WITHOUT having knowledge of internal code structure, implementation details and internal paths.",
    "Non-Functionalities of software applications are tested WITHOUT having knowledge of internal code structure, implementation details and internal paths.",
    "Functionalities of software applications are tested WITH having knowledge of internal code structure, implementation details and internal paths.",
    "Non-Functionalities of software applications are tested WITH having knowledge of internal code structure, implementation details and internal paths.",
]


class TestValidrequireds:
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.get("https://sandbox.moodledemo.net/")
        self.driver.set_window_size(1850, 1048)
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("sandbox")
        self.driver.find_element(By.ID, "loginbtn").click()
        self.driver.find_element(By.LINK_TEXT, "My first course").click()
        self.driver.find_element(By.NAME, "setmode").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#coursecontentcollapse0 .activity-add-text"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".option:nth-child(15) .optionicon > .icon"
        ).click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("My first quiz")
        self.driver.find_element(By.ID, "id_submitbutton").click()
        self.driver.find_element(By.LINK_TEXT, "Add question").click()
        self.driver.find_element(
            By.XPATH, "//a[@id='action-menu-toggle-1']/span"
        ).click()
        self.driver.find_element(By.ID, "actionmenuaction-1").click()
        self.driver.find_element(By.ID, "item_qtype_multichoice").click()
        self.driver.find_element(By.NAME, "submitbutton").click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("Introduction")
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
        element = self.driver.find_element(By.ID, "tinymce")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'What is Black-box testing?'}",
            element,
        )
        self.driver.switch_to.default_content()

    def teardown_method(self, method):
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.driver.quit()

    @pytest.mark.parametrize(
        "questions",
        [
            [
                (TEXTS[0], None),
                (TEXTS[1], 100),
                (TEXTS[2], None),
                (TEXTS[3], None),
            ],
            [
                (TEXTS[0], 100),
                (TEXTS[1], 100),
                (TEXTS[2], 100),
            ]
        ],
        ids=["full", "all 100"]
    )
    def test_valid(self, questions):
        for (i, (text, grade)) in enumerate(questions):
            self.driver.switch_to.frame((i + 1) * 2)
            self.driver.find_element(By.CSS_SELECTOR, "p").click()
            element = self.driver.find_element(By.ID, "tinymce")
            self.driver.execute_script(
                f"if(arguments[0].contentEditable === 'true') {{arguments[0].innerText = '{text}'}}",
                element,
            )
            self.driver.switch_to.default_content()
            if grade is not None:
                dropdown = self.driver.find_element(By.ID, "id_fraction_1")
                dropdown.find_element(By.XPATH, f"//option[. = '{grade}%']").click()
        
        self.driver.find_element(By.ID, "id_submitbutton").click()
        assert (
            self.driver.find_element(By.CSS_SELECTOR, "span.questiontext").text
            == "What is Black-box testing?"
        )

    @pytest.mark.parametrize(
        "questions",
        [
            [
                (TEXTS[0], 100),
            ],
            [
                (TEXTS[0], 100),
                (None, 100),
            ],
            [
                (TEXTS[0], None),
                (TEXTS[1], -50),
                (TEXTS[2], 50),
                (TEXTS[3], -100),
            ],
        ],
        ids=["only one", "missing text", "no 100"]
    )
    def test_invalid(self, questions):
        for (i, (text, grade)) in enumerate(questions):
            self.driver.switch_to.frame((i + 1) * 2)
            self.driver.find_element(By.CSS_SELECTOR, "p").click()
            element = self.driver.find_element(By.ID, "tinymce")
            if text is not None:
                self.driver.execute_script(
                    f"if(arguments[0].contentEditable === 'true') {{arguments[0].innerText = '{text}'}}",
                    element,
                )
            self.driver.switch_to.default_content()
            if grade is not None:
                dropdown = self.driver.find_element(By.ID, "id_fraction_1")
                dropdown.find_element(By.XPATH, f"//option[. = '{grade}%']").click()
        
        self.driver.find_element(By.ID, "id_submitbutton").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.invalid-feedback")
        assert len(elements) > 0
