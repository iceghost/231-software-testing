import XLUtils
import time
import os
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

def get_local_path():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return current_dir

def get_file_path(filename):
    current_dir = get_local_path()
    current_file_path = os.path.join(current_dir, filename)
    if os.path.exists(current_file_path):
        return current_file_path
    else:
        return ('file path does not exist')

class TestFilePlugin():

  course = "bk" 
  driver = webdriver.Chrome()
  driver.implicitly_wait(5)

  def admin_setfile_allow_size(self):
    self.driver.delete_all_cookies()
    self.driver.get("https://sandbox.moodledemo.net/")
    self.driver.set_window_size(1382, 1382)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.ID, "password").send_keys("sandbox")
    self.driver.find_element(By.ID, "loginbtn").click()

    self.driver.find_element(By.LINK_TEXT, "My first course").click()
    self.driver.find_element(By.LINK_TEXT, "Settings").click()

    # self.driver.find_element(By.XPATH, "//div[@id=\'action_bar\']/div[2]/form/button").click()

    # time.sleep(2)
    # self.driver.find_element(By.ID, "id_fullname").send_keys(self.course)
    # self.driver.find_element(By.ID, "id_shortname").send_keys(self.course)
    
    # time.sleep(2)
    # self.driver.execute_script("window.scrollTo(0,9000)")
    # time.sleep(2)

    self.driver.find_element(By.ID, "collapseElement-4").click()
    self.driver.find_element(By.ID, "id_maxbytes").click()
    
    if self.driver.find_element(By.ID, "id_maxbytes").is_displayed():
      dropdown = self.driver.find_element(By.ID, "id_maxbytes")
      select = Select(dropdown)
      time.sleep(2)
      select.select_by_visible_text("10 KB")
    self.driver.find_element(By.ID, "id_saveanddisplay").click()

  def test_filePlugin(self,filename):    
    self.driver.delete_all_cookies()
    self.driver.get("https://sandbox.moodledemo.net/")
    self.driver.set_window_size(1382, 1382)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "username").send_keys("teacher")
    self.driver.find_element(By.ID, "password").send_keys("sandbox")
    self.driver.find_element(By.ID, "loginbtn").click()

    self.driver.find_element(By.LINK_TEXT, "My courses").click()

    self.driver.find_element(By.LINK_TEXT, "My first course").click()
    time.sleep(2)

    webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    # self.driver.find_element(By.XPATH, "//div/div/input").click()
    self.driver.find_element(By.NAME, "setmode").click()
    self.driver.find_element(By.CSS_SELECTOR, "#coursecontentcollapse0 .activity-add-text").click()
    self.driver.find_element(By.XPATH, "//div[7]/div/a/div/img").click()
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("FilePlugin1")
    self.driver.find_element(By.ID, "id_name").send_keys(Keys.ENTER)
    
    
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".dndupload-message .fa").click()
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Upload a file\')]").click()
    
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(get_file_path(filename))
    time.sleep(3)
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Upload this file\')]").click()
    time.sleep(3)  
   
    # # self.driver.find_element(By.NAME, "\"repo_upload_file\"").click()
    # # self.driver.find_element(By.NAME, "\"repo_upload_file\"").send_keys("C:\\fakepart\\1_Byte.txt")
    self.driver.find_element(By.ID, "id_submitbutton").click()
  

test = TestFilePlugin()
# test.course = namecourse
# test.admin_setfile_allow_size()
# test.test_filePlugin("1byte.txt")
# test.test_filePlugin("2byte.txt")
# test.test_filePlugin("10Kb_plus1byte.txt")
# test.test_filePlugin("10Kb_sub_1byte")
# test.test_filePlugin("10Kb.txt")
# test.test_filePlugin("5Kb.txt")

def is_element_clickable(xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        if element.is_displayed():
            return True
        return False
    except Exception:
        return False


path = "./BinhKhang.xlsx"

rows = XLUtils.getRowCount(path, 'UploadAssignmentUsecase')

for r in range(2, rows+1):
    file_path = XLUtils.readData(path, 'FilePlugin(teacher)', r, 2)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://sandbox.moodledemo.net/")
    driver.set_window_size(1382, 1382)
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "username").send_keys("teacher")
    driver.find_element(By.ID, "password").send_keys("sandbox")
    driver.find_element(By.ID, "loginbtn").click()

    driver.find_element(By.LINK_TEXT, "My courses").click()

    driver.find_element(By.LINK_TEXT, "My first course").click()
    time.sleep(2)

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # driver.find_element(By.XPATH, "//div/div/input").click()
    driver.find_element(By.NAME, "setmode").click()
    driver.find_element(By.CSS_SELECTOR, "#coursecontentcollapse0 .activity-add-text").click()
    driver.find_element(By.XPATH, "//div[7]/div/a/div/img").click()
    driver.find_element(By.ID, "id_name").click()
    driver.find_element(By.ID, "id_name").send_keys("FilePlugin1")
    driver.find_element(By.ID, "id_name").send_keys(Keys.ENTER)
    
    
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".dndupload-message .fa").click()
    driver.find_element(By.XPATH, "//a[contains(.,\'Upload a file\')]").click()
    
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(get_file_path(file_path))
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(.,\'Upload this file\')]").click()
    time.sleep(3)  
   
    # # driver.find_element(By.NAME, "\"repo_upload_file\"").click()
    # # driver.find_element(By.NAME, "\"repo_upload_file\"").send_keys("C:\\fakepart\\1_Byte.txt")

    if is_element_clickable(driver.find_element(By.ID, "id_submitbutton")):
      driver.find_element(By.ID, "id_submitbutton").click()
      XLUtils.writeData(path, 'UploadAssignmentUsecase', r, 3, "PASSED")
    else:
      XLUtils.writeData(path, 'UploadAssignmentUsecase', r, 3, "FAILED")
   