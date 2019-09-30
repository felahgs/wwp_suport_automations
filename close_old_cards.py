 # in a given time 

import time, sys, os, re, datetime

from pageobjects.trello import login
from pageobjects.trello import board
from pageobjects.wwp import login
from pageobjects.wwp import source


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from api import trello

from utils import date

if __name__ == "__main__":

    my_date = date.dateChecker()
    start = my_date.convert_to_date("09/09/2019")
    end = my_date.convert_to_date("13/09/2019")
    days = my_date.get_days_beetween(start, end)
    # print('\n Verifying the following dates \n', days)

    trello = trello.TrelloApi()
    done_cards = trello.get_done_cards_obj(days, 'open')

    print('Closing cards from', start, 'to', end)
    for card in done_cards:
        print(card, 'closed')
        text = '**Automation: Closing cards**\n' + 'Closed all done cards from ' + str(start) + ' to ' + str(end)
        card.comment(text)
        card.set_closed(True)
