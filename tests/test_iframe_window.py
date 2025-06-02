from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.chrome.service import Service
from utils.driver import getChromeDriver
import time

# Setup WebDriver
driver = getChromeDriver()
driver.get("https://demoqa.com/browser-windows")

def test_tabs():
    # Click on 'New Tab' and handle the new tab
    driver.find_element(By.ID, "tabButton").click()
    time.sleep(2)  # Wait for the new tab to open
    driver.switch_to.window(driver.window_handles[-1])  # Switch to the new tab
    print("Title of new tab:", driver.title)
    driver.close()  # Close the new tab
    driver.switch_to.window(driver.window_handles[0])  # Switch back to the original window


def test_new_window():
    # Click on 'New Window' and handle the new window
    driver.find_element(By.ID, "windowButton").click()
    time.sleep(2)  # Wait for the new window to open
    driver.switch_to.window(driver.window_handles[-1])  # Switch to the new window
    print("Title of new window:", driver.title)
    driver.close()  # Close the new window
    driver.switch_to.window(driver.window_handles[0])  # Switch back to the original window

def test_iframe():
    # Click on 'New Window Message' and handle the new window with message
    driver.find_element(By.ID, "messageWindowButton").click()
    time.sleep(2)  # Wait for the new window to open
    driver.switch_to.window(driver.window_handles[-1])  # Switch to the new window
    print("Title of new window with message:", driver.title)
    driver.close()  # Close the new window
    driver.switch_to.window(driver.window_handles[0])  # Switch back to the original window
