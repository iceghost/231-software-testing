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
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("sandbox")
driver.find_element(By.ID, "loginbtn").click()
driver.find_element(By.LINK_TEXT, "Site administration").click()
driver.find_element(By.LINK_TEXT, "Users").click()
driver.find_element(By.LINK_TEXT, "Browse list of users").click()
driver.find_element(By.XPATH, "//button[contains(.,\'Add a new user\')]").click()
driver.find_element(By.ID, "id_username").send_keys("teacher1")
time.sleep(2)
driver.find_element(By.XPATH, "//em[contains(.,'Click to enter text')]").click()
driver.find_element(By.ID, "id_newpassword").send_keys("123456")
driver.find_element(By.ID, "id_firstname").send_keys("Teacher")
driver.find_element(By.ID, "id_lastname").send_keys("Teacher")
driver.find_element(By.ID, "id_email").send_keys("abc@abc.com")
driver.find_element(By.ID, "id_submitbutton").click()
driver.find_element(By.XPATH, "//a[contains(.,\'Courses\')]").click()
driver.find_element(By.LINK_TEXT, "Manage courses and categories").click()
driver.find_element(By.XPATH, "//a[contains(.,\'My second course\')]").click()
driver.find_element(By.XPATH, "//a[contains(.,\'Enrolled users\')]").click()
driver.find_element(By.CSS_SELECTOR, "#enrolusersbutton-1 .btn").click()
driver.find_element(By.XPATH, "//div[3]/input").send_keys("abc@abc.com")
driver.find_element(By.XPATH, "//div[2]/div/div[2]/ul/li").click()
driver.find_element(By.CSS_SELECTOR, "#fitem_id_roletoassign > .col-md-9").click()
driver.find_element(By.ID, "id_roletoassign").click()
Select(driver.find_element(By.NAME, "roletoassign")).select_by_visible_text("Teacher")
driver.find_element(By.XPATH, "//a[contains(.,\'Show more...\')]").click()
driver.find_element(By.XPATH, "//*[@id=\"id_startdate\"]/option[1]").click()
driver.find_element(By.XPATH, "//button[contains(.,\'Enrol users\')]").click()
driver.delete_all_cookies()
driver.get("https://sandbox.moodledemo.net/")
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.ID, "username").send_keys("teacher")
driver.find_element(By.ID, "password").send_keys("sandbox")
driver.find_element(By.ID, "loginbtn").click()
driver.find_element(By.LINK_TEXT, "My courses").click()
driver.find_element(By.LINK_TEXT, "My first course").click()
driver.find_element(By.NAME, "setmode").click()
driver.find_element(By.CSS_SELECTOR, "#coursecontentcollapse0 .activity-add-text").click()
driver.find_element(By.LINK_TEXT, "Assignment").click()
driver.find_element(By.ID, "id_name").send_keys("Assignment 1")
driver.find_element(By.ID, "id_submitbutton2").click()

data_path = "Hai.xlsx"
rows = XLUtils.getRowCount(data_path, "GradeAssignment")

for row in range(2, rows + 1):
    username = XLUtils.readData(data_path, "GradeAssignment", row, 1)
    password = XLUtils.readData(data_path, "GradeAssignment", row, 2)
    grade = XLUtils.readData(data_path, "GradeAssignment", row, 3)

    driver.delete_all_cookies()
    driver.get("https://sandbox.moodledemo.net/")
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginbtn").click()
    driver.find_element(By.LINK_TEXT, "My courses").click()

    if (element_exits("My first course")):
        driver.find_element(By.LINK_TEXT, "My first course").click()
        driver.find_element(By.LINK_TEXT, "Assignment 1").click()
        driver.find_element(By.LINK_TEXT, "View all submissions").click()
        driver.find_element(By.LINK_TEXT, "Grade").click()
        ele = driver.find_element(By.ID, "id_grade")
        ele.clear()
        ele.send_keys(grade)
        driver.find_element(By.NAME, "savechanges").click()
  
