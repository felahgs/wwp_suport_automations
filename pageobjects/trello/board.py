from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pageobjects.basepage import BasePage


class BoardPage(BasePage):
    PAGE_CONTENT = (By.CLASS_NAME, 'board-main-content')
    URL = "https://trello.com/b/cPsGnXpd/iss-sm-wls-source-fixing-qa-fail"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_page(self):
        self.driver.get(BoardPage.URL)
        print ("Navigating to in to", BoardPage.URL)
        self.wait.until(EC.presence_of_element_located(BoardPage.PAGE_CONTENT))

    # def get_cards(self, board):
    #     cards = self.driver.find_elements(*CustomerGroupsPage.CUSTOMER_GROUP)

        