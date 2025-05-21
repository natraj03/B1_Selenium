from utils.mydriver import getChromeDriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


myDriver = getChromeDriver()

def openLoginPage():
    myDriver.get("http://65.0.30.232:8090/login")
    time.sleep(5)
def username(username):
    myDriver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)

def password(password):
    myDriver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

def signIn():
    myDriver.find_element(By.XPATH,"//div[@class='login-form--footer']//input[@name='login']").click()

def forgetPassword():
    myDriver.find_element(By.XPATH,"//div[@class='login-links']/a[@href='/account/lost_password']").click()

def createNweAccount():
    myDriver.find_element(By.XPATH,"//div[@class='login-links']/a[@title='Create a new account']").click()

