import time

from pages.login import  *
from pages.create_task import  *
from pages.dashboard import  *
from utils.driver import getChromeDriver
import openpyxl
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
env_email = os.getenv("email")
env_password = os.getenv("password")
workbook = None
driver1 = None
driver2 = None

def setup_function():
    global driver1
    driver1 = getChromeDriver()
    global driver2
    driver2 = getChromeDriver()
    global workbook
    workbook = openpyxl.load_workbook("../Data/Automation_Task_Data.xlsx")


def teardown_function():
    global driver
    # if driver:
        # driver.quit()
    global workbook
    if workbook:
        workbook.close()


def test_2_windows():

    login_d1 = Login(driver1)
    login_d1.openLoginPage()
    login_d1.username(env_email)
    login_d1.password(env_password)
    login_d1.signIn()
    dashboard_d1 = Dashboard(driver1)
    dashboard_d1.openMyproject()
    # first_tab = driver.current_window_handle

    driver1.execute_script(f"window.open('{work_packages_url}');")
    time.sleep(5)

    tabs = driver1.window_handles
    print("check windows",tabs)
    driver1.switch_to.window(tabs[1])
    dashboard_d1.openPackages()
    dashboard_d1.clickCreatebutton()
    dashboard_d1.clickCreatebutton_task()
    taskObj_d1 = CreateTask(driver1)
    taskObj_d1.taskName("First window task")
    taskObj_d1.description("First window description")

    driver1.switch_to.window(tabs[0])
    time.sleep(20)

    driver1.switch_to.window(tabs[1])
    time.sleep(5)

    taskObj_d1.assigneUser("Rashmi Sahoo")
    taskObj_d1.assigneAccountability("Rashmi Sahoo")
    taskObj_d1.workHours(10)
    taskObj_d1.remainingWork(10)

    # -----------------Driver 2 / 2nd window-------------------
    login_d2 = Login(driver2)
    login_d2.openLoginPage()
    login_d2.username(env_email)
    login_d2.password(env_password)
    login_d2.signIn()
    dashboard_d2 = Dashboard(driver2)
    dashboard_d2.openMyproject()
    # first_tab = driver.current_window_handle

    driver2.execute_script(f"window.open('{work_packages_url}');")
    time.sleep(5)

    tabs2 = driver2.window_handles
    print("check windows", tabs)
    driver2.switch_to.window(tabs2[1])
    dashboard_d2.openPackages()
    dashboard_d2.clickCreatebutton()
    dashboard_d2.clickCreatebutton_task()
    taskObj_d2 = CreateTask(driver2)
    taskObj_d2.taskName("Second Window Task")
    taskObj_d2.description("Second window Description")

    driver2.switch_to.window(tabs2[0])
    time.sleep(20)

    driver2.switch_to.window(tabs2[1])
    time.sleep(5)

    taskObj_d2.assigneUser("Srikanta Bisoyi")
    taskObj_d2.assigneAccountability("Srikanta Bisoyi")
    taskObj_d2.workHours(10)
    taskObj_d2.remainingWork(10)