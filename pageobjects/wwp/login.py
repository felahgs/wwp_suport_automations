
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pageobjects.basepage import BasePage
from pageobjects.wwp import dashboard

class LoginPage(BasePage):
    LOGIN_SCREEN = (By.CLASS_NAME, 'container-fluid')
    INPUT_ACCESS_CODE = (By.ID, 'accessCode')
    INPUT_USER_NAME = (By.ID, 'userName')
    INPUT_PASSWORD = (By.ID, 'password')
    BTN_LOGIN = (By.ID,'login')
    LOGIN_ERROR = (By.ID, "lert-danger")
    URL = "https://sm.worldwatchplus.com/"


    def __init__(self, driver):
        self.driver = driver
        # self.URL = 'https://cinq.repairq.io/site/login'
        self.wait = WebDriverWait(driver, 10)
        LoginPage.navigate_to_page(self)
        self.wait.until(EC.presence_of_element_located(LoginPage.LOGIN_SCREEN))

    def navigate_to_page(self):
        self.driver.get(LoginPage.URL)
        self.wait.until(EC.presence_of_element_located(LoginPage.LOGIN_SCREEN))

    def set_username(self, username):
        elem = self.driver.find_element(*LoginPage.INPUT_USER_NAME)
        elem.send_keys(username)

    def set_access_code(self, accessCode):
        elem = self.driver.find_element(*LoginPage.INPUT_ACCESS_CODE)
        elem.send_keys(accessCode)

    def set_password(self, password):
        elem = self.driver.find_element(*LoginPage.INPUT_PASSWORD)
        elem.send_keys(password)

    def try_to_login (self, accessCode, username, password):
        LoginPage.navigate_to_page(self)
        LoginPage.set_access_code(self, accessCode)
        LoginPage.set_username(self, username)
        LoginPage.set_password(self, password)
        btn = self.driver.find_element(*LoginPage.BTN_LOGIN)
        btn.click()
        print ("Logging in to", LoginPage.URL)
        dashboard_menu = dashboard.DashboardMenu(self.driver)
        # print('printing', *dashboard_menu.SIDEBAR)
        try:
            self.wait.until(EC.visibility_of_element_located((dashboard_menu.SIDEBAR)))
        except TimeoutException:
            error = self.driver.find_element(LoginPage.LOGIN_ERROR)
            print('Login Error:', error.get_attribute("innerHTML") )
            error = self.driver.find_element_by_class_name('help-inline')
            return False
        else:
            print('Trello Login Success')
            return dashboard_menu

            