import time
from selenium.webdriver.common.by import By



class Logout:
    def __init__(self, driver):
        self.driver = driver

    def openDashboardPage(self):
        self.driver.get("http://65.0.30.232:8090/")
        time.sleep(5)

    def userMenuLogo(self):
        self.driver.find_element(By.XPATH,
                                 "//div[@class='op-principal--avatar op-avatar op-avatar_default op-avatar_user op-avatar--fallback']").click()

    def signout(self):
        self.driver.find_element(By.XPATH, "//a[@class='logout-menu-item op-menu--item-action']").click()

