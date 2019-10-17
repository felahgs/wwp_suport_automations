import time, sys, os, re, datetime

from pageobjects.trello import login
from pageobjects.trello import board
from pageobjects.wwp import login
from pageobjects.wwp import source


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from api import trello

class Portal():
    def __init__(self):
        print("Initializing webdriver\n")

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        ## Disable devTools
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(chrome_options=options)
        # self.driver = webdriver.Chrome()
        
        self.login_page = login.LoginPage(self.driver)

    def login(self):
        self.login_page.navigate_to_page()
        self.login_page.try_to_login('cinq', 'felipes', 'cinq12345')

    def get_source_status(self, source_name):
        source_name = source.SourceInfo(self.driver, source_name)
        return source_name.get_status(self.driver)

    def get_source_name(self, source_name):
        source_name = source.SourceInfo(self.driver, source_name)
        return source_name.get_name(self.driver)

    def get_source_priority(self, source_name):
        source_name = source.SourceInfo(self.driver, source_name)
        return source_name.get_priority(self.driver)
        
    def fetch_board_sources(self):
        board_page = board.BoardPage(self.driver)
        board_page.navigate_to_page()

    def end(self):
        print("\nClosing browser")
        time.sleep(7)
        self.driver.quit()
        exit(0)