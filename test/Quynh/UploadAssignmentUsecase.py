import XLUtils
import time
import os


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)


def get_local_path():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return current_dir


def get_file_path(filename):
    current_dir = get_local_path()
    current_file_path = os.path.join(current_dir, filename)
    if os.path.exists(current_file_path):
        return current_file_path
    else:
        return "file path does not exist"


def is_element_clickable(xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        if element.is_displayed():
            return True
        return False
    except Exception:
        return False


# get link browser test
# driver.get("")

driver.get("https://sandbox.moodledemo.net/")
# driver.get("https://sandbox402.moodledemo.net/")
driver.set_window_size(1000, 728)

# Log in as teacher
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.ID, "username").send_keys("teacher")
driver.find_element(By.ID, "password").send_keys("sandbox")
driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

driver.find_element(By.LINK_TEXT, "My courses").click()
driver.find_element(By.LINK_TEXT, "My first course").click()
time.sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

driver.find_element(By.XPATH, "//div/div/input").click()

# Add assignment 1
driver.find_element(
    By.CSS_SELECTOR, "#coursecontentcollapse0 .activity-add-text"
).click()
driver.find_element(By.LINK_TEXT, "Assignment").click()

time.sleep(2)
driver.find_element(By.ID, "id_name").send_keys("Assignment 1")


Select(driver.find_element(By.NAME, "duedate[year]")).select_by_value("2024")

# Disable remind me to grade
driver.find_element(By.XPATH, "//input[@id='id_gradingduedate_enabled']").click()

# Choose document type
driver.find_element(By.XPATH, "//fieldset/div/span/input").click()
driver.find_element(By.XPATH, "//div[6]/label/input").click()
driver.find_element(By.XPATH, "//button[contains(.,'Save changes')]").click()

# Save assignment 1
driver.find_element(By.ID, "id_submitbutton2").click()

# Add assignment 2
driver.find_element(
    By.CSS_SELECTOR, "#coursecontentcollapse0 .activity-add-text"
).click()
driver.find_element(By.LINK_TEXT, "Assignment").click()

time.sleep(2)
driver.find_element(By.ID, "id_name").send_keys("Assignment 2")

# Change from to to 2022
Select(driver.find_element(By.NAME, "allowsubmissionsfromdate[year]")).select_by_value(
    "2022"
)
Select(driver.find_element(By.NAME, "duedate[year]")).select_by_value("2022")

# Choose document type
driver.find_element(By.XPATH, "//fieldset/div/span/input").click()
driver.find_element(By.XPATH, "//div[6]/label/input").click()
driver.find_element(By.XPATH, "//button[contains(.,'Save changes')]").click()

# Save assignment 2
driver.find_element(By.ID, "id_submitbutton2").click()


# Login as student
driver.delete_all_cookies()
driver.get("https://sandbox.moodledemo.net/")
# driver.get("https://sandbox402.moodledemo.net/")
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("sandbox")
driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

# Add submission
driver.find_element(By.LINK_TEXT, "My courses").click()
driver.find_element(By.LINK_TEXT, "My first course").click()
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

driver.find_element(By.LINK_TEXT, "Assignment 1").click()
driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()

# duong dan file excel
path = "Quynh.xlsx"

rows = XLUtils.getRowCount(path, "UploadAssignmentUsecase")

for r in range(2, rows + 1):
    choice = XLUtils.readData(path, "UploadAssignmentUsecase", r, 1)

    time.sleep(1)
    if choice == "Yes":
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".fa-file-o").click()
        driver.find_element(By.XPATH, "//a[contains(.,'Upload a file')]").click()

        rela_path = XLUtils.readData(path, "UploadAssignmentUsecase", r, 2)
        file_path = get_file_path(rela_path)

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)

        time.sleep(3)
        driver.find_element(
            By.XPATH, "//button[contains(.,'Upload this file')]"
        ).click()
        time.sleep(3)

        if is_element_clickable("//div[3]/div/div/span/button"):
            time.sleep(2)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            XLUtils.writeData(path, "UploadAssignmentUsecase", r, 3, "FAILED")

        else:
            XLUtils.writeData(path, "UploadAssignmentUsecase", r, 3, "PASSED")

            driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]').click()

            # Remove file to continue test
            time.sleep(5)
            driver.find_element(
                By.XPATH, "//button[contains(.,'Remove submission')]"
            ).click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
            time.sleep(2)
            driver.find_element(
                By.XPATH, "//button[contains(.,'Add submission')]"
            ).click()

    else:
        driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(2)
        driver.find_element(By.ID, "id_cancel").click()
        time.sleep(2)
        XLUtils.writeData(path, "UploadAssignmentUsecase", r, 3, "FAILED")
