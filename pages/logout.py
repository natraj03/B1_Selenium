from utils.mydriver import getChromeDriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


myDriver = getChromeDriver()

def openDashboardPage():
    myDriver.get("http://65.0.30.232:8090/")
    time.sleep(5)
def userMenuLogo():
    myDriver.find_element(By.XPATH, "//div[@class='op-principal--avatar op-avatar op-avatar_default op-avatar_user op-avatar--fallback']").click()



