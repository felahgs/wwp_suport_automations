# import sys

# from trello import TrelloClient
# from api import trello
# from automation import wwp

# import argparse

# if __name__ == "__main__":

#     parser = argparse.ArgumentParser()

#     parser.add_argument("-bye", help="Run all scripts", action="end_of_day")

#     args = parser.parse_args()

#     print(args.square**2)

 # in a given time 

import time, sys, os, re

from datetime import date

from trello import TrelloClient

from automation import wwp
from api import trello

from pageobjects.trello import login
from pageobjects.trello import board
from pageobjects.wwp import login
from pageobjects.wwp import source

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# from utils import date

if __name__ == "__main__":

    number_renamed_cards = 0

    trello = trello.TrelloApi()
    
    automation = wwp.Portal()
    automation.login()

    columns_list = ["Waiting Web Fetcher", "Daily Review", "Need Review - New Configuration Rejected by Web Fetcher - EXTRACT/Structured", "Needs Review - Crawl/RIP", "Needs Development", "Technical Review (Tommy)", "Business Review - Pending", "Business Review - Already Checked", "Paused"]
    
    for queue in columns_list:
        queue = [bucket for bucket in trello.my_lists if queue in bucket.name]
        print("Checking cards in", queue[0].name + "\n")
        for card in queue[0].list_cards():
            card_name = card.name.split()[0]
            new_name = card_name
            print(new_name)
            card.set_name(new_name)
            number_renamed_cards += 1
            
    print("\n\n" + "***** Number of renamed cards: " + str(number_renamed_cards) + " ***** \n")

    automation.end()
