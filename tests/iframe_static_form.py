from selenium.webdriver.common.by import By
from utils.driver import getChromeDriver
import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Setup WebDriver
driver = getChromeDriver()
driver.get(f"file:///{script_dir}/../resources/framefile.html")  # Update with the correct path
# driver.get("file:///Users/apple/Documents/python_project/Task_1/openProject_Class/resources/myform.html")

# def test_sendEmail():
#     time.sleep(5)
#     driver.find_element(By.XPATH, '//input[@id="email"]').send_keys("rashmi@test.com")




def test_iframe():
    time.sleep(5)
    driver.find_element(By.ID,"mainIplPage").click()
    # Switch to the second iframe (Registration Form)
    driver.switch_to.window(driver.window_handles[0])  # Switch back to the original window

    driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
    time.sleep(5)
    # Fill in the registration form
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "email").send_keys("testuser@test.com")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.switch_to.default_content()

    # Switch to the first iframe (Static Links)
    time.sleep(5)
    driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[1])

    # Click on the first link (Example Website)
    driver.find_element(By.XPATH, '//a[@href="https://www.github.com"]').click()

    # Switch back to the main content
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.default_content()
    time.sleep(5)
    driver.find_element(By.ID, "pointsTable").click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    #

