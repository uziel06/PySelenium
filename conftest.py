import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC


username = "uziel.dreisbach" # Replace the username
access_key = "Ae2CFun58ihGjl1Ovf088VZVRMerhH3fRWhf0F6DSPZGiqS8vO" # Replace the access key

@pytest.fixture(scope="class")
def setup_chrome(request):
    chromeOptions = webdriver.ChromeOptions()
    chrome_options = {
        "username": username,
        "accessKey": access_key,
        "platform": "Windows 10",
        "browserName": "Chrome",
        "version": "86.0",
        "visual": True,
        "video": True,
        "resolution": "1280x1024",
        "network": True,
        "build": "AssignmentTask",
        "name": "ChromeWindowsExecution",
        "project": "MySeleniumCertification",
        "console": "error",
        "w3c": True,
        "plugin": "python-python",
        "selenium_version": "4.0.0",
    }
    chromeOptions.set_capability('LT:Options', chrome_options)
    driver = webdriver.Remote(
        command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
            username, access_key), options = chromeOptions)

    driver.set_page_load_timeout(20)
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/")
    scrolltoAllIntegration = driver.find_element(By.CSS_SELECTOR, "div[class*='clearfix'] a[href*='https://www.lambdatest.com/integrations']")
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class*='clearfix'] a[href*='https://www.lambdatest.com/integrations']")))
    action = AC(driver)
    action.move_to_element(scrolltoAllIntegration)
    action.perform()

    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="class")
def setup_edge(request):
    edgeOptions = webdriver.EdgeOptions()
    edge_options = {
        "username": username,
        "accessKey": access_key,
        "platform": "macOS Sierra",
        "browserName": "Edge",
        "version": "87.0",
        "visual": True,
        "video": True,
        "resolution": "1280x1024",
        "network": True,
        "build": "AssignmentTask",
        "name": "EdgeMacOSExecution",
        "project": "MySeleniumCertification",
        "console": "error",
        "w3c": True,
        "plugin": "python-python",
        "selenium_version": "4.0.0",
    }
    edgeOptions.set_capability('LT:Options', edge_options)
    driver = webdriver.Remote(
        command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
            username, access_key), options = edgeOptions)

    driver.set_page_load_timeout(20)
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/")
    scrolltoAllIntegration = driver.find_element(By.CSS_SELECTOR, "div[class*='clearfix'] a[href*='https://www.lambdatest.com/integrations']")
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class*='clearfix'] a[href*='https://www.lambdatest.com/integrations']")))
    action = AC(driver)
    action.move_to_element(scrolltoAllIntegration)
    action.perform()

    request.cls.driver = driver
    yield
    driver.close()



