import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pageobjects.basepage import BasePage
from pageobjects.wwp import dashboard

class LoginPage(BasePage):
    LOGIN_SCREEN = (By.CLASS_NAME, "app")
    INPUT_USER_NAME = (By.ID, 'i0116')
    INPUT_PASSWORD = (By.ID, 'i0118')
    BTN_LOGIN = (By.ID,'idSIButton9')
    LOGIN_ERROR = (By.CLASS_NAME, "alert-error")
    URL = "https://web.skype.com/"


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

    def try_to_login (self, username, password):
        LoginPage.navigate_to_page(self)

        LoginPage.set_username(self, username)
        btn = self.driver.find_element(*LoginPage.BTN_LOGIN)
        btn.click()

        self.wait.until(EC.presence_of_element_located(LoginPage.INPUT_PASSWORD))
        LoginPage.set_password(self, password)
        time.sleep(2)
        btn = self.driver.find_element(*LoginPage.BTN_LOGIN)
        btn.click()
        
        print ("Logging in to", LoginPage.URL, '\n')
        dashboard_menu = dashboard.DashboardMenu(self.driver)
        try:
            self.wait.until(EC.url_to_be(LoginPage.URL))

        except TimeoutException:
            error = self.driver.find_element(LoginPage.LOGIN_ERROR)
            print('Login Error:', error.get_attribute("innerHTML") )
            return False
        else:
            print('WWP Source Management Login Success\n')
            return dashboard_menu

            