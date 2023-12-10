import XLUtils
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)


# get link browser test
# driver.get("")

driver.get("https://sandbox.moodledemo.net/")
driver.set_window_size(1382, 744)
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.ID, "username").send_keys("teacher")
driver.find_element(By.ID, "password").send_keys("sandbox")
driver.find_element(By.ID, "loginbtn").click()

driver.find_element(By.LINK_TEXT, "My courses").click()

driver.find_element(By.LINK_TEXT, "My first course").click()
time.sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

# edit
driver.find_element(By.NAME, "setmode").click()


driver.find_element(By.CLASS_NAME, "activity-add-text").click()


driver.find_element(By.LINK_TEXT, "Assignment").click()


driver.find_element(By.ID, "id_name").send_keys("Test Assignment 1")
driver.find_element(By.ID, "id_submitbutton2").click()

# driver.find_element(By.NAME, "setmode").click()

WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Test Assignment 1"))
).click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.aalink stretched-link[href]"))).click()

driver.find_element(By.LINK_TEXT, "View all submissions").click()
driver.find_element(By.LINK_TEXT, "Grade").click()


# duong dan file excel
path = "Quynh.xlsx"


rows = XLUtils.getRowCount(path, "GradeAssignment")

for r in range(2, rows + 1):
    grade = XLUtils.readData(path, "GradeAssignment", r, 2)

    elem = driver.find_element(By.NAME, "grade")
    elem.clear()
    elem.send_keys(grade)

    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "savechanges"))).click()

    driver.find_element(By.NAME, "savechanges").click()
    time.sleep(3)

    if driver.find_element(By.ID, "id_error_grade").is_displayed():
        XLUtils.writeData(path, "GradeAssignment", r, 3, "FAILED")
    else:
        XLUtils.writeData(path, "GradeAssignment", r, 3, "PASSED")
