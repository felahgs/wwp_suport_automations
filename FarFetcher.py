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

    trello = trello.TrelloApi()
    
    number_renamed_cards = 0
    labels_add = []
    labels_remove = []
    labels_remove.append(trello.get_label("High"))
    labels_remove.append(trello.get_label("Medium"))
    labels_remove.append(trello.get_label("Low"))
    labels_remove.append(trello.get_label("New"))
    labels_remove.append(trello.get_label("QA-Fail"))
    labels_remove.append(trello.get_label("Ops-Fail"))
    labels_remove.append(trello.get_label("IT-Review"))
    
    automation = wwp.Portal()
    automation.login()

    columns_list = ["Needs Review - Crawl/RIP", "Needs Development", "NMedia - No New Records", "Business Review - Pending", "Business Review - Already Checked", "Paused", "Technical Review (Tommy)"]
    # columns_list = ["Backlog"]
    
    for queue in columns_list:
        queue = [bucket for bucket in trello.my_lists if queue in bucket.name]
        print("Checking cards in", queue[0].name + "\n")
        for card in queue[0].list_cards():
            card_name = card.name.split()[0]
            status = automation.get_source_status(card_name)
            # if (("WATCH" in card_name) and ("IT-Review" in status)):
            #     print(card_name, status)
            #     for remove in labels:
            #         card.remove_label(remove)
            #     card.add_label(trello.get_label("IT-Review"))
            #     card.change_pos("top")
            #     number_renamed_cards += 1
            priority = automation.get_source_priority(card_name)
            print(card_name, status, priority)
            if not (("On-line" in status) or ("In-Progress" in status) or (priority is None)):
                if "xPath Error" in status:
                    status = "QA-Fail"
                labels_add.append(trello.get_label(priority))
                labels_add.append(trello.get_label(status))
                for remove in labels_remove:
                    card.remove_label(remove)
                for add in labels_add:
                    card.add_label(add)
            labels_add.pop()
            labels_add.pop()
            number_renamed_cards += 1


    print("\n\n" + "***** Number of renamed cards: " + str(number_renamed_cards) + " ***** \n")

    automation.end()
