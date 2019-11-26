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

    # number_verifying_card = 1
    number_filed_cards = 0
    total_filed_cards = 0

    trello = trello.TrelloApi()

    date = date.today().strftime("%d/%m/%Y")

    fila_desejada = input("Enter column name to parse: ")

    if ((fila_desejada == "all") or (fila_desejada == "All")):

        automation = wwp.Portal()
        automation.login()

        print("Closing inactive cards")
        waiting_web_fetcher_list = ["Backlog", "Peer Review", "In Progress", "Waiting Web Fetcher", "Daily Review", "Need Review - New Configuration Rejected by Web Fetcher - EXTRACT/Structured", "Needs Review - Crawl/RIP", "Needs Development", "Business Review - Already Checked", "Paused", "Technical Review (Tommy)"]
        for queue in waiting_web_fetcher_list:
            queue = [bucket for bucket in trello.my_lists if queue in bucket.name]
            print("Checking cards in", queue[0].name + "\n")
            # number_verifying_card = 0
            number_filed_cards = 0
            for card in queue[0].list_cards():
                card_name = card.name.split()[0]
                status = automation.get_source_status(card_name)
                # print(card_name, status)
                # if (number_verifying_card % 5 == 0):
                #     print("Verifying card " + str(number_verifying_card))
                # number_verifying_card += 1
                if "Inactive" in status:
                    new_name = card_name + " - Closed in " + date
                    # print("\n" + card_name, status)
                    print(card_name, status)
                    card.set_name(new_name)
                    text = "Automation: Closing Inactive Cards**\n" + "Card " + card_name + " is in " + status
                    card.comment(text)
                    card.set_closed(True)
                    number_filed_cards += 1
                    
            total_filed_cards += number_filed_cards

            print("\n\n" + "***** Number of closed cards in " + queue[0].name + ": " + str(number_filed_cards) + " ***** \n")
        print("\n\n" + "***** Number of closed cards in total" + ": " + str(total_filed_cards) + " ***** \n")

    else:
        waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if fila_desejada in bucket.name]

        while (("Checked" in str(waiting_web_fetcher_list)) or ("NMedia" in str(waiting_web_fetcher_list)) or ("Records" in str(waiting_web_fetcher_list)) or ("Live" in str(waiting_web_fetcher_list))):
            if "Checked" in str(waiting_web_fetcher_list):
                print("*** Attention, the column 'Business Review - Already Checked' can not be parsed. ***" + "\n")
            if "Live" in str(waiting_web_fetcher_list):
                print("*** Attention, the column 'Live' can not be parsed. ***" + "\n")
            else:
                print("*** Attention, the column 'NMedia - No New Records' can not be parsed. ***" + "\n")
            fila_desejada = input("Enter column name to parse: ")
            waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if fila_desejada in bucket.name]

        print("Checking cards in", waiting_web_fetcher_list[0].name)

        automation = wwp.Portal()
        automation.login()

        for card in waiting_web_fetcher_list[0].list_cards():
            card_name = card.name.split()[0]
            status = automation.get_source_status(card_name)
            # print(card_name, status)
            # if (number_verifying_card % 5 == 0):
            #     print("Verifying card " + str(number_verifying_card))
            # number_verifying_card += 1
            if "Inactive" in status:
                new_name = card_name + " - Closed in " + date
                # print("\n" + card_name, status)
                print(card_name, status)
                card.set_name(new_name)
                text = "**Automation: Closing Inactive Cards**\n" + "Card " + card_name + " is in " + status
                card.comment(text)
                card.set_closed(True)
                total_filed_cards += 1
        
        print("\n\n" + "***** Number of closed cards: " + str(total_filed_cards) + " ***** \n")

    automation.end()