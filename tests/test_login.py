from pages.login import  *
from utils.driver import getChromeDriver

driver = None
def setup_function():
    global driver
    driver = getChromeDriver()


def teardown_function():
    global driver
    # if driver:
        # driver.quit()

def test_success():
    loginObj = Login(driver)
    loginObj.openLoginPage()
    loginObj.username("rashmiranjan4546@gmail.com")
    loginObj.password("Nist@12345")
    loginObj.signIn()
    loginObj.openMyproject()

