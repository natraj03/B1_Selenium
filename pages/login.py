import time
from Constants.configs import base_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login:
    
    def __init__(self, driver):
        self.driver = driver

    def openMyproject(self):
        self.driver.get(f"{base_URL}/projects/5/?jump=angular")
        # http://65.0.30.232:8090/projects/5/?jump=angular
        time.sleep(5)

    def openLoginPage(self):
        self.driver.get(f"{base_URL}/login")
        time.sleep(5)

    def username(self,username):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)

    def password(self,password):
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

    def signIn(self):
        self.driver.find_element(By.XPATH, "//div[@class='login-form--footer']//input[@name='login']").click()
        time.sleep(5)

    def forgetPassword(self):
        self.driver.find_element(By.XPATH, "//div[@class='login-links']/a[@href='/account/lost_password']").click()

    def createNweAccount(self):
        self.driver.find_element(By.XPATH, "//div[@class='login-links']/a[@title='Create a new account']").click()
