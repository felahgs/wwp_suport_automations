
import time, sys, os, re, datetime

from pageobjects.trello import login
from pageobjects.trello import board
from pageobjects.wwp import login
from pageobjects.wwp import source


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from trello import TrelloClient


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

class TrelloApi():
    def __init__(self):
        # https://trello.com/app-key
        client = TrelloClient(
            api_key='ca43dd546a8464cf0b7564e0f392dbd1',
            api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
        )

        self.all_boards = client.list_boards()
        self.wls_board = self.all_boards[1]
        self.my_lists = self.wls_board.list_lists()

    def get_done_cards(self, days):
        done_sources = []
        print('Searching Trello cards..\n')
        for list in self.my_lists:
            for card in list.list_cards(card_filter='all'):
                if "Done" in card.name: 
                    name = card.name.split()[0]
                    date = re.compile('[0-9]{2}/[0-9]{2}/[0-9]{2,4}')
                    date = date.findall(card.name)[0]
                    # print(name, date)
                    if date in days:
                        # done_sources.append(name + ' ' + date)
                        done_sources.append(name)
                    # exit(0)
                    # print(card.name)
        return done_sources

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
    start = my_date.convert_to_date("19/08/2019")
    end = my_date.convert_to_date("19/08/2019")
    days = my_date.get_days_beetween(start, end)
    print(days)

    trello = TrelloApi()
    done_cards = trello.get_done_cards(days)
    print(done_cards)

    automation = Portal()
    automation.login()
    for card in done_cards:
        name = automation.get_source_name(card)
        status = automation.get_source_status(card)
        print(name, status)
    automation.end()

    # for card in done_cards:
    #     print(card, end = ' ')
    # print('\n')
