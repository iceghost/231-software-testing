from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import XLUtils


driver = webdriver.Chrome()
# driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("https://sandbox.moodledemo.net/")
driver.set_window_size(1000, 744)
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.ID, "username").send_keys("teacher")
driver.find_element(By.ID, "password").send_keys("sandbox")
driver.find_element(By.ID, "loginbtn").click()
driver.find_element(By.LINK_TEXT, "My courses").click()
driver.find_element(By.LINK_TEXT, "My first course").click()
driver.find_element(By.NAME, "setmode").click()

data_path = "Hai.xlsx"
rows = XLUtils.getRowCount(data_path, "CreateQuiz")

for row in range(2, rows + 1):
    name = XLUtils.readData(data_path, "CreateQuiz", row, 1)
    time_limit = XLUtils.readData(data_path, "CreateQuiz", row, 2)

    driver.find_element(By.CSS_SELECTOR, "#coursecontentcollapse0 .activity-add-text").click()
    driver.find_element(By.LINK_TEXT, "Quiz").click()
    driver.find_element(By.ID, "id_name").send_keys(name)
    driver.find_element(By.ID, "collapseElement-1").click()
    driver.find_element(By.CSS_SELECTOR, "#fitem_id_timelimit .form-check").click()
    driver.find_element(By.ID, "id_timelimit_number").send_keys(time_limit)
    driver.find_element(By.ID, "id_submitbutton2").click()
  
