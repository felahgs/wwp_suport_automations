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

    number_verifying_card = 1
    number_moved_cards = 0
    number_filed_cards = 0

    trello = trello.TrelloApi()

    date = date.today().strftime("%d/%m/%Y")

    # my_date = date.dateChecker()

    # cards_number = 0

    # data_inicio = input("\n" + "Digite a data inicial de armazenamento dos cards: ")
    # data_fim = input("\n" + "Digite a data final de armazenamento dos cards: ")
    # if((data_inicio != "") and (data_fim != "")):
    #     dia_inicio = int(my_date.convert_to_date(data_inicio).strftime("%d"))
    #     dia_fim = int(my_date.convert_to_date(data_fim).strftime("%d"))

    # while ((data_inicio == "") or (data_fim == "") or (data_fim < data_inicio)):
    #     if((data_inicio == "") or (data_fim == "")):
    #         print ("\n" + "Favor digitar as datas de inicio e fim para o armazenamento dos cards")
            
    #     else:
    #         print("\n" + "Favor digitar uma data final maior que a data inicial")

    #     data_inicio = input("\n" + "Digite a data inicial de armazenamento dos cards: ")
    #     data_fim = input("\n" + "Digite a data final de armazenamento dos cards: ")
    #     if((data_inicio != "") and (data_fim != "")):
    #         dia_inicio = int(my_date.convert_to_date(data_inicio).strftime("%d"))
    #         dia_fim = int(my_date.convert_to_date(data_fim).strftime("%d"))


    # # data_inicio = my_date.convert_to_date("23/09/2019")
    # # data_fim = my_date.convert_to_date("27/09/2019")
    # days = my_date.get_days_beetween(my_date.convert_to_date(data_inicio), my_date.convert_to_date(data_fim))
    # # print("\n Verifying the following dates \n", days)

    # trello = trello.TrelloApi()
    # done_cards = trello.get_done_cards_obj(days, "open")

    # print("Closing cards from", data_inicio, "to", data_fim)
    # for card in done_cards:
    #     print(card, "closed")
    #     text = "**Automation: Closing cards**\n" + "Closed all done cards from " + str(data_inicio) + " to " + str(data_fim)
    #     card.comment(text)
    #     cards_number += 1
    #     card.set_closed(True)

    # print("\n" + "Numero de cards arquivados: " + cards_number)

    business_list = [bucket for bucket in trello.my_lists if "Business Review - Already Checked" in bucket.name]
    peer_list = [bucket for bucket in trello.my_lists if "Peer Review" in bucket.name]

    automation = wwp.Portal()
    automation.login()
    
    print("Clearing column 'Business Review - Already Checked'..." + "\n")

    for card in business_list[0].list_cards():
        card_name = card.name.split()[0]
        status = automation.get_source_status(card_name)
        if (number_verifying_card % 5 == 0):
            print("Verifying card " + str(number_verifying_card))
        number_verifying_card += 1
        if (("Inactive" in status) or ("On-line" in status)):
            print("\n" + card_name, status)
            text = "Automation: Check Business Queue**" + "\n" + "Card " + card_name + " is " + status + "\n" + "Filed in " + date
            card.comment(text)
            print(text, "\n")
            card.set_closed(True)
            number_filed_cards += 1
        else:
            new_name = card_name + " - Already Checked"
            print("\n" + card_name, status)
            card.set_name(new_name)
            card.change_list(peer_list[0].id)
            card.change_pos("top")
            text = "Automation: Check Business Queue**" + "\n" + "Card " + card_name + " is " + status + "\n" + "Moved to " + peer_list[0].name
            card.comment(text)
            print(text, "\n")
            number_moved_cards += 1

    print("\n\n" + "***** Number of filed cards: " + str(number_filed_cards) + " ***** \n")
    print("***** Number of moved cards: " + str(number_moved_cards) + " ***** \n")
