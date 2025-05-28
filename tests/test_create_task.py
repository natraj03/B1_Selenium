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
driver = None
def setup_function():
    global driver
    driver = getChromeDriver()
    global workbook
    workbook = openpyxl.load_workbook("../Data/Automation_Task_Data.xlsx")


def teardown_function():
    global driver
    # if driver:
        # driver.quit()
    global workbook
    if workbook:
        workbook.close()



def test_open_project():
    login = Login(driver)
    login.openLoginPage()
    login.username(env_email)
    login.password(env_password)
    login.signIn()
    dashboard = Dashboard(driver)
    dashboard.openMyproject()
    #
    # sheet = workbook["Sheet1"]
    # index = 0
    # for row in sheet.iter_rows(values_only=True):
    #     print("row",row)
    #     if index > 0 and index < 6:
    #         pass
    #         dashboard.openPackages()
    #         dashboard.clickCreatebutton()
    #         dashboard.clickCreatebutton_task()
    #         taskObj = CreateTask(driver)
    #         taskObj.taskName(row[0])
    #         taskObj.description(row[1])
    #         taskObj.assigneUser(row[2])
    #         taskObj.assigneAccountability(row[3])
    #         taskObj.workHours(row[4])
    #         taskObj.remainingWork(row[5])
    #         taskObj.clickDateandSetTFDate(row[6],row[7])
    #         taskObj.setPriority(row[8])
    #         taskObj.savetask()
    #
    #     elif index > 5:
    #         break
    #     index += 1