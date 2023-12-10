from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import XLUtils
import time


def element_exits(path):
    try:
        element = driver.find_element(By.LINK_TEXT, path)
        if element.is_displayed(): return True
        else: return False
    except Exception:
        return False

driver = webdriver.Chrome()
# driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("https://sandbox.moodledemo.net/")
driver.set_window_size(1053, 728)
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.ID, "username").send_keys("teacher")
driver.find_element(By.ID, "password").send_keys("sandbox")
driver.find_element(By.ID, "loginbtn").click()
driver.find_element(By.LINK_TEXT, "My courses").click()
driver.find_element(By.LINK_TEXT, "My first course").click()
driver.find_element(By.NAME, "setmode").click()
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
driver.find_element(By.CSS_SELECTOR, "#coursecontentcollapse0 .activity-add-text").click()
driver.find_element(By.LINK_TEXT, "Assignment").click()
driver.find_element(By.ID, "id_name").send_keys("Assignment 1")
driver.find_element(By.ID, "id_submitbutton2").click()

data_path = "Hai.xlsx"
rows = XLUtils.getRowCount(data_path, "GradeAssignmentUsecaseTesting")

for row in range(2, rows + 1):
    test_flow = XLUtils.readData(data_path, "GradeAssignmentUsecaseTesting", row, 1)
    grade = XLUtils.readData(data_path, "GradeAssignmentUsecaseTesting", row, 2)

    driver.delete_all_cookies()
    driver.get("https://sandbox.moodledemo.net/")
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "username").send_keys("teacher")
    driver.find_element(By.ID, "password").send_keys("sandbox")
    driver.find_element(By.ID, "loginbtn").click()
    driver.find_element(By.LINK_TEXT, "My courses").click()
    driver.find_element(By.LINK_TEXT, "My first course").click()
    driver.find_element(By.LINK_TEXT, "Assignment 1").click()
    if (test_flow == "Alter2"):
        driver.find_element(By.LINK_TEXT, "Grade").click()
        ele = driver.find_element(By.ID, "id_grade")
        ele.clear()
        ele.send_keys(grade)
        driver.find_element(By.NAME, "savechanges").click()
        continue
        
    driver.find_element(By.LINK_TEXT, "View all submissions").click()

    if (test_flow == "Alter1"):
        driver.find_element(By.LINK_TEXT, "Edit").click()
        driver.find_element(By.CSS_SELECTOR, "#action-menu-1-menu > a:nth-child(1)").click()
        ele = driver.find_element(By.ID, "id_grade")
        ele.clear()
        ele.send_keys(grade)
        driver.find_element(By.NAME, "savechanges").click()
        continue

    elif (test_flow == "Alter3"):
        driver.find_element(By.ID, "selectuser_4").click()
    
    driver.find_element(By.LINK_TEXT, "Grade").click()
    ele = driver.find_element(By.ID, "id_grade")
    ele.clear()
    ele.send_keys(grade)

    if (test_flow == "Alter4"):
        driver.find_element(By.NAME, "saveandshownext").click()
        continue
    elif (test_flow == "Alter5"):
        driver.find_element(By.NAME, "resetbutton").click()
        continue
    driver.find_element(By.NAME, "savechanges").click()
  
