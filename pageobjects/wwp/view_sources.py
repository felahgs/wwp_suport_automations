
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pageobjects.basepage import BasePage

class ViewSources(BasePage):

    numbers = (By.XPATH, "//small[contains(text(),'Total Sources')]")
    # numbers_IT = (By.XPATH, "//small[contains(text(),"Total Sources")]")
    # numbers_QA_Low = (By.XPATH, "//")
    # numbers_QA_Medium = (By.XPATH, "//")
    # numbers_QA_High = (By.XPATH, "//")

    SIDEBAR = (By.CLASS_NAME, "sidebar-sticky")
    URL = "https://sm.worldwatchplus.com/main1.php?app=viewSrc&mod=wls&advSearch=1&sourceQueues="

    # IT = URL + "6&page=1"
    # QA_Low = URL + "3&sourcePriorities=3&page=1"
    # QA_Medium = URL + "3&sourcePriorities=2&page=1"
    # QA_High = URL + "3&sourcePriorities=1&page=1"


    def __init__(self, driver, queue, priority):
        self.driver = driver
        self.queue = queue
        self.priority = priority
        # self.wait = WebDriverWait(driver, 10)
        # self.wait.until(EC.presence_of_element_located(DashboardMenu.SIDEBAR))

    def navigate_to_page(self):
        self.driver.get(ViewSources.URL)
        # self.wait.until(EC.presence_of_element_located(ViewSources.SIDEBAR))

    def check_url(self):
        if "IT" in self.queue:
            queue_id = "6"
            ViewSources.URL = ViewSources.URL + queue_id + "&page=1"
        elif "QA" in self.queue :
            queue_id = "3"
            if "Low" in self.priority:
                priority_id = "3"
            elif "Medium" in self.priority:
                priority_id = "2"
            elif "High" in self.priority:
                priority_id = "1"
            else: 
                priority_id = "error"
            ViewSources.URL = ViewSources.URL + queue_id + "&sourcePriorities=" + priority_id + "&page=1"

    def get_numbers(self, driver):
        self.check_url()
        if self.driver.current_url is not ViewSources.URL:
            self.navigate_to_page()
        try:
            queue_numbers = driver.find_element(*ViewSources.numbers).get_attribute("innerHTML")
        except NoSuchElementException:
            return "NOT FOUND"
        return queue_numbers

    # def get_qa_low_numbers(self, driver):
    #     ViewSources.URL = ViewSources.QA_Low

    #     if self.driver.current_url is not ViewSources.URL:
    #         self.navigate_to_page()
    #     try:
    #         qa_low_number = driver.find_element(*ViewSources.numbers).get_attribute("innerHTML")
    #     except NoSuchElementException:
    #         return "NOT FOUND"
    #     return qa_low_number

    # def get_qa_medium_numbers(self, driver):
    #     ViewSources.URL = ViewSources.QA_Medium

    #     if self.driver.current_url is not ViewSources.URL:
    #         self.navigate_to_page()
    #     try:
    #         qa_medium_number = driver.find_element(*ViewSources.numbers).get_attribute("innerHTML")
    #     except NoSuchElementException:
    #         return "NOT FOUND"
    #     return qa_medium_number

    # def get_qa_high_numbers(self, driver):
    #     ViewSources.URL = ViewSources.QA_High

    #     if self.driver.current_url is not ViewSources.URL:
    #         self.navigate_to_page()
    #     try:
    #         qa_high_number = driver.find_element(*ViewSources.numbers).get_attribute("innerHTML")
    #     except NoSuchElementException:
    #         return "NOT FOUND"
    #     return qa_high_number

    
            