import XLUtils

from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestCase

driver = webdriver.Chrome()

# get link browser test
# driver.get("")

driver.get("https://sandbox.moodledemo.net/")
driver.set_window_size(1382, 744)
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("sandbox")
driver.find_element(By.ID, "loginbtn").click()
driver.find_element(By.LINK_TEXT, "Site administration").click()
driver.find_element(By.LINK_TEXT, "Payment accounts").click()


# duong dan file excel
path = "Quynh.xlsx"


rows = XLUtils.getRowCount(path, "CreatePaymentAccount")

for r in range(2, rows + 1):
    name = XLUtils.readData(path, "CreatePaymentAccount", r, 1)
    id = XLUtils.readData(path, "CreatePaymentAccount", r, 2)

    driver.find_element(
        By.XPATH, "//button[contains(.,'Create payment account')]"
    ).click()
    driver.find_element(By.ID, "id_name").send_keys(name)
    driver.find_element(By.ID, "id_idnumber").send_keys(id)

    driver.find_element(By.ID, "id_submitbutton").click()

    if driver.find_element(By.CLASS_NAME, "h2").text == "Payment accounts":
        XLUtils.writeData(path, "CreatePaymentAccount", r, 3, "PASSED")
    else:
        XLUtils.writeData(path, "CreatePaymentAccount", r, 3, "FAILED")
        driver.find_element(By.ID, "id_cancel").click()
