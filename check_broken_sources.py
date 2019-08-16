
import time, sys, os

from pageobjects.trello import login
from pageobjects.trello import board

from selenium import webdriver
from selenium.webdriver.common.by import By

from trello import TrelloClient


class Test():
    def __init__(self):
        print("Initializing webdriver\n")
        self.driver = webdriver.Chrome()

    def login_trello(self):
        login_page = login.LoginPage(self.driver)
        login_page.navigate_to_page()
        login_page.try_to_login('fgsouza93@gmail.com', 'Tje3qz%e')

    def fetch_board_sources(self):
        board_page = board.BoardPage(self.driver)
        board_page.navigate_to_page()

    def end(self):
        print("\nClosing browser")
        time.sleep(7)
        self.driver.quit()
        exit(0)


if __name__ == "__main__":

    client = TrelloClient(
        api_key='ca43dd546a8464cf0b7564e0f392dbd1',
        api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
    )

    all_boards = client.list_boards()
    wls_board = all_boards[1]
    my_lists = wls_board.list_lists()

    done_sources = []

    for list in my_lists:
        for card in list.list_cards(card_filter='all'):
            if "Done" in card.name: 
                # print(card.name.split()[1])
                done_sources.append(card.name.split()[1])

    print(done_sources)
    print(done_sources[1])
    
