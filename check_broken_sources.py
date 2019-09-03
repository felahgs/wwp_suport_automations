
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

class dateChecker():
    def daterange(self, date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + datetime.timedelta(n)

    def get_days_beetween(self, date1, date2):
        days = []
        for dt in self.daterange(date1, date2):
            # print(dt.strftime("%d/%m/%y"))
            days.append(dt.strftime("%d/%m/%Y"))
        return days

    def convert_to_date(self, date):
        dd = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%d'))
        mm = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m'))
        yyyy = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%Y'))
        return datetime.date(yyyy,mm,dd)


if __name__ == "__main__":
    

    my_date = dateChecker()
    start = my_date.convert_to_date("28/06/2019")
    end = my_date.convert_to_date("28/06/2019")
    days = my_date.get_days_beetween(start, end)
    print('\n Verifying the following dates \n', days)

    trello = trello.TrelloApi()
    done_cards = trello.get_done_cards(days)
    print(done_cards)

    automation = Portal()
    automation.login()
    for card in done_cards:
        name = automation.get_source_name(card)
        status = automation.get_source_status(card)
        print(card, status)
    automation.end()

    # for card in done_cards:
    #     print(card, end = ' ')
    # print('\n')
