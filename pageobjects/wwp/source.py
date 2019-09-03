
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pageobjects.basepage import BasePage 

class SourceInfo(BasePage):
    WWP_ID = (By.XPATH, "//div[@class='table-responsive']/table/tbody/tr[2]/td[1]")
    SOURCE_ID = (By.XPATH, "//div[@class='table-responsive']/table/tbody/tr[2]/td[2]")
    PRIORITY = (By.XPATH, "//div[@class='table-responsive']/table/tbody/tr[2]/td[3]")
    QUEUE = (By.XPATH, "//div[@class='table-responsive']/table/tbody/tr[2]/td[4]")
    AGENCY = (By.XPATH, "//div[@class='table-responsive']/table/tbody/tr[6]/td[1]")
    TYPE = (By.XPATH, "//div[@class='table-responsive']/table/tbody/tr[8]/td[1]")

    MAIN_URL = "https://sm.worldwatchplus.com/viewSourceDetails.php?mod="
    URL = ""


    def __init__(self, driver, source_name):
        self.driver = driver
        self.source_name = source_name

    def navigate_to_page(self):
        self.driver.get(SourceInfo.URL)

    def check_url(self):
        if 'WATCH' in self.source_name:
            product = 'wls'
        elif 'GOV' in self.source_name :
            product = 'gov'
        elif 'MEDIA' in self.source_name:
            product = 'media'

        SourceInfo.URL = SourceInfo.MAIN_URL + product + '&sourceId=' + self.source_name

    def get_status(self, driver):
        self.check_url()
        if self.driver.current_url is not SourceInfo.URL:
            self.navigate_to_page()
        try:
            status = driver.find_element(*SourceInfo.QUEUE).get_attribute('innerHTML')
        except NoSuchElementException:
            return "NOT FOUND"
        return status

    def get_name(self, driver):
        self.check_url()
        if self.driver.current_url is not SourceInfo.URL:
            self.navigate_to_page()
        try:        
            source_id = driver.find_element(*SourceInfo.SOURCE_ID).get_attribute('innerHTML')
        except NoSuchElementException:
            return "NOT FOUND" 
        # print('SOURCE_ID', source_id)
        # print(SourceInfo.URL + '\n')
        return source_id

    def get_priority(self, driver):
        self.check_url()
        if self.driver.current_url is not SourceInfo.URL:
            self.navigate_to_page()        
        try: 
            priority = driver.find_element(*SourceInfo.PRIORITY).get_attribute('innerHTML').strip()
        except NoSuchElementException:
            return "NOT FOUND"
        return priority

        
    
            # MEDIA_US_4890