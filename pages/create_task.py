import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateTask:
    def __init__(self, driver):
        self.driver = driver


    def taskName(self,taskName):
        time.sleep(10)
        self.driver.find_element(By.XPATH,'//input[@id="wp-new-inline-edit--field-subject"]').send_keys(taskName)

    def description(self,desc):
        time.sleep(1)
        # self.driver.find_element(By.XPATH,'//div[@class="ck-blurred document-editor__editable op-uc-container op-uc-container_editing ck ck-content ck-editor__editable ck-rounded-corners ck-editor__editable_inline"]').send_keys(desc)
        descElement = self.driver.find_element(By.XPATH,'//p[@class="op-uc-p"]')
        descElement.send_keys(desc)

    def assigneUser(self,value):
        time.sleep(1)
        assignXpath = '//ng-select[@id="wp-new-inline-edit--field-assignee"]'
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, assignXpath))
        )
        dropdown.click()
        assignXpath2 = f'{assignXpath}//input'

        # Step 2: Type in the input field to search
        input_box = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, assignXpath2))
        )
        input_box.clear()
        input_box.send_keys(value)
        time.sleep(1)
        # Step 3: Wait for the dropdown options and click the first one
        option_xpath = "//ng-dropdown-panel//div[contains(@class, 'ng-option') and @role='option'][1]"
        option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option.click()


    def assigneAccountability(self, value):
        time.sleep(1)
        assignXpath = '//ng-select[@id="wp-new-inline-edit--field-responsible"]'
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, assignXpath))
        )
        dropdown.click()

        # Step 2: Type in the input field to search
        input_box = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"{assignXpath}//input"))
        )
        input_box.clear()
        input_box.send_keys(value)
        time.sleep(1)
        # Step 3: Wait for the dropdown options and click the first one
        option_xpath = "//ng-dropdown-panel//div[contains(@class, 'ng-option') and @role='option'][1]"
        option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option.click()

    def workHours(self, hours):
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//input[@id="wp-new-inline-edit--field-estimatedTime"]').send_keys(hours)

    def remainingWork(self,hours):
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//input[@id="wp-new-inline-edit--field-remainingTime"]').send_keys(hours)

    def clickDateandSetTFDate(self, startDate,endDate):
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//input[@class="spot-input"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//input[@class="spot-text-field--input ng-untouched ng-pristine ng-valid" and @name="startDate"]').send_keys(startDate)
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//input[@class="spot-text-field--input ng-untouched ng-pristine ng-valid" and @name="endDate"]').send_keys(endDate)
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//button[@class="button -highlight spot-action-bar--action"]').click()

    def setPriority(self, value):
        time.sleep(1)

        # scrollable_div = self.driver.find_element(By.XPATH, "//div[contains(@class, 'scroll-host')]")
        assignXpath = '//ng-select[@class="inline-edit--field priority ng-select-searchable ng-select ng-select-single ng-untouched ng-pristine ng-valid"]'

        self.driver.execute_script("arguments[0].scrollTop += 100", assignXpath)

        time.sleep(1)
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, assignXpath))
        )
        dropdown.click()

        # # Step 2: Type in the input field to search
        # input_box = WebDriverWait(self.driver, 5).until(
        #     EC.visibility_of_element_located((By.XPATH, f"{assignXpath}//input"))
        # )
        # input_box.clear()
        # input_box.send_keys(value)
        time.sleep(1)
        # Step 3: Wait for the dropdown options and click the first one
        option_xpath = f"//ng-dropdown-panel//div[contains(@class, 'ng-option') and @role='option']//span[text()='{value}']"
            # f"//ng-dropdown-panel//div[contains(@class, 'ng-option') and @role='option' .//div[@title={value}]"
        print("option_xpath for priority",option_xpath)
        option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option.click()

    def savetask(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//button[@id="work-packages--edit-actions-save"]').click()