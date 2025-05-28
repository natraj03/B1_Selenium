import time
from selenium.webdriver.common.by import By
from Constants.configs import base_URL


class Logout:
    def __init__(self, driver):
        self.driver = driver

    def openDashboardPage(self):
        self.driver.get(f"{base_URL}")
        time.sleep(5)

    def userMenuLogo(self):
        self.driver.find_element(By.XPATH,
                                 "//div[@class='op-principal--avatar op-avatar op-avatar_default op-avatar_user op-avatar--fallback']").click()

    def signout(self):
        self.driver.find_element(By.XPATH, "//a[@class='logout-menu-item op-menu--item-action']").click()

