import time
from selenium.webdriver.common.by import By
from Constants.configs import base_URL



class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    def openMyproject(self):
        self.driver.get(f"{base_URL}/projects/5/?jump=angular")
        # http://65.0.30.232:8090/projects/5/?jump=angular
        time.sleep(5)

    def userMenuLogo(self):
        self.driver.find_element(By.XPATH, "//div[@class='op-principal--avatar op-avatar op-avatar_default op-avatar_user op-avatar--fallback']").click()

    def clickWorkSpace(self):
        self.driver.find_element(By.XPATH,"//a[@id='main-menu-work-packages']").click()
        time.sleep(5)
    def clickCreatebutton(self):
        # self.driver.find_element(By.XPATH,"//button[@class='button -alt-highlight add-work-package']").click()
        self.driver.find_element(By.XPATH, '//button[@class="button -alt-highlight add-work-package"]').click()
        time.sleep(2)
    def clickCreatebutton_task(self):
        # //a[@class="menu-item __hl_inline_type_1"]
        self.driver.find_element(By.XPATH,"//a[@href='/projects/batch-b1/work_packages/create_new?type=1']").click()

    def openPackages(self):
        self.driver.get(f"{base_URL}/projects/batch-b1/work_packages")
        time.sleep(10)