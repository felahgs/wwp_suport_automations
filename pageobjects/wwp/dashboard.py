
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pageobjects.basepage import BasePage

class DashboardMenu(BasePage):
    SIDEBAR = (By.CLASS_NAME, 'sidebar-sticky')
    URL = "https://sm.worldwatchplus.com/main1.php?app=dashboard"


    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(driver, 10)
        # self.wait.until(EC.presence_of_element_located(DashboardMenu.SIDEBAR))

    def navigate_to_page(self):
        self.driver.get(LoginPage.URL)
        self.wait.until(EC.presence_of_element_located(DashboardMenu.SIDEBAR))

    
            