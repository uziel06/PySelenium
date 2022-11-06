from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.mark.usefixtures('setup_chrome')
class TestAssignment():
    def test_seeAllIntegration(self):
        #Allowing cookies
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Allow Cookie']"))).click()
        
        #clicking on See All Integration and opening it to new window
        seeAllIntegration = self.driver.find_element(By.CSS_SELECTOR, "div[class*='clearfix'] a[href*='https://www.lambdatest.com/integrations']")
        action = AC(self.driver)
        action.key_down(Keys.CONTROL)
        action.click(seeAllIntegration)
        action.key_up(Keys.CONTROL)
        action.perform()
    
    def test_windowHandles(self):
        expectedWindowHandles = ['https://www.lambdatest.com/', 'https://www.lambdatest.com/integrations']
        switchWindow = self.driver.switch_to.window
        windowsOpened = self.driver.window_handles
        windowList = []
    
        #Saving window handles in a List
        for windows in windowsOpened:
            windowList.append(windows)
            print(str(windowList))

        switchWindow(windowsOpened[1])
        currentOpenedURL = self.driver.current_url

        if currentOpenedURL in expectedWindowHandles:
            print("Current URL is in Expected Window Handles")
        else:
            assert currentOpenedURL not in expectedWindowHandles
            print("Current opened URL is not in the Expected Window Handles")
        print(currentOpenedURL)

        #Scroll to Codeless Automation
        codelessAutomation = self.driver.find_element(By.ID, "codeless_row")
        action = AC(self.driver)
        action.move_to_element(codelessAutomation)
        action.click(codelessAutomation)
        action.perform()

        #checking the title
        pageTitle = self.driver.title
        expectedPageTitle = "TestingWhiz Integration | LambdaTest"
        print(pageTitle)

        if pageTitle == expectedPageTitle:
            print("Page title is same with Expected title")
        else:
            assert pageTitle != expectedPageTitle
            print("Page title is not equal to Expected Page Title")

        #closing current window
        self.driver.close()
        switchWindow(windowsOpened[0])

    #changing url to lambdatest blog
    def test_changeURL(self):
        self.driver.get("https://www.lambdatest.com/blog")
        self.driver.find_element(By.XPATH, "//div[@class='menu-menu-1-container']//ul//li[5]/a[text()='Community']").click()
        currentURL = self.driver.current_url
        print(currentURL)
        assert currentURL == "https://community.lambdatest.com/"



        



    