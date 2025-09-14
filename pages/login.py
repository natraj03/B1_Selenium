from utils.mydriver import getChromeDriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


myDriver = getChromeDriver()

def openMyproject():
    myDriver.get("http://65.0.30.232:8090/projects/5/?jump=angular")
    # http://65.0.30.232:8090/projects/5/?jump=angular
    time.sleep(5)
def openLoginPage():
    myDriver.get("http://65.0.30.232:8090/login")
    time.sleep(5)
def username(username):
    myDriver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)

def password(password):
    myDriver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

def signIn():
    myDriver.find_element(By.XPATH,"//div[@class='login-form--footer']//input[@name='login']").click()
    time.sleep(5)

def forgetPassword():
    myDriver.find_element(By.XPATH,"//div[@class='login-links']/a[@href='/account/lost_password']").click()

def createNweAccount():
    myDriver.find_element(By.XPATH,"//div[@class='login-links']/a[@title='Create a new account']").click()

def openDashboardPage():
    myDriver.get("http://65.0.30.232:8090/")
    time.sleep(5)
def userMenuLogo():
    myDriver.find_element(By.XPATH, "//div[@class='op-principal--avatar op-avatar op-avatar_default op-avatar_user op-avatar--fallback']").click()

def signout():
    myDriver.find_element(By.XPATH,"//a[@class='logout-menu-item op-menu--item-action']").click()

def clickWorkSpace():
    # //a[@id="main-menu-work-packages"]
    myDriver.find_element(By.XPATH,"//a[@id='main-menu-work-packages']").click()
    time.sleep(5)
def clickCreatebutton():
    # //button[@class="button -alt-highlight add-work-package"]
    myDriver.find_element(By.XPATH,"//button[@class='button -alt-highlight add-work-package']").click()
    time.sleep(2)
def clickCreatebutton_task():
    # //a[@class="menu-item __hl_inline_type_1"]
    myDriver.find_element(By.XPATH,"//a[@href='/projects/batch-b1/work_packages/create_new?type=1']").click()

def new Task():
    myDriver.find_element()
