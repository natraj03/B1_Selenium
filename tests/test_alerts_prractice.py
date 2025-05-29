import time
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

def test_alerts():

    driver.get("https://demoqa.com/alerts")
    time.sleep(30)
    scrollTilElement = '//button[@id="promtButton"]'
    driver.execute_script("arguments[0].scrollTop += 100", scrollTilElement)

    # ---------- Simple Alert ----------
    # Click the button to trigger a simple alert
    driver.find_element(By.ID, "alertButton").click()
    time.sleep(1)

    # Switch to alert and accept
    alert = driver.switch_to.alert
    print("Simple Alert Text:", alert.text)
    alert.accept()

    # ---------- Confirmation Alert ----------
    # Click the button to trigger confirm box
    driver.find_element(By.ID, "confirmButton").click()
    time.sleep(1)

    # Handle confirm alert (accept or dismiss)
    confirm_alert = driver.switch_to.alert
    print("Confirmation Alert Text:", confirm_alert.text)
    confirm_alert.accept()  # or confirm_alert.dismiss()

    # ---------- Prompt Alert ----------
    # Click the button to trigger prompt box
    driver.find_element(By.ID, "promtButton").click()
    time.sleep(1)

    # Handle prompt alert
    prompt_alert = driver.switch_to.alert
    print("Prompt Alert Text:", prompt_alert.text)
    prompt_alert.send_keys("Selenium Test")
    time.sleep(15)
    # prompt_alert.accept()

    # Clean up
    # time.sleep(2)
    # driver.quit()
