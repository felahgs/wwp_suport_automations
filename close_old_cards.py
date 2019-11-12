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

    print("Starting Script: Closing Old Cards...")

    my_date = date.dateChecker()

    cards_number = 0

    data_inicio = input("\n" + "Enter the initial closing cards date: ")
    data_fim = input("\n" + "Enter the final closing cards date: ")
    if((data_inicio != "") and (data_fim != "")):
        dia_inicio = int(my_date.convert_to_date(data_inicio).strftime("%Y/%m/%d").replace("/",""))
        dia_fim = int(my_date.convert_to_date(data_fim).strftime("%Y/%m/%d").replace("/",""))

    while ((data_inicio == "") or (data_fim == "") or (dia_fim < dia_inicio)):
        if((data_inicio == "") or (data_fim == "")):
            print ("\n" + "Please enter the initial and final closing cards date.")
            
        else:
            print("\n" + "Please enter a final date higher then the initial one.")

        data_inicio = input("\n" + "Enter the initial closing cards date: ")
        data_fim = input("\n" + "Enter the final closing cards date: ")
        if((data_inicio != "") and (data_fim != "")):
            dia_inicio = int(my_date.convert_to_date(data_inicio).strftime("%d"))
            dia_fim = int(my_date.convert_to_date(data_fim).strftime("%d"))


    # data_inicio = my_date.convert_to_date("23/09/2019")
    # data_fim = my_date.convert_to_date("27/09/2019")
    days = my_date.get_days_beetween(my_date.convert_to_date(data_inicio), my_date.convert_to_date(data_fim))
    # print("\n Verifying the following dates \n", days)

    trello = trello.TrelloApi()
    done_cards = trello.get_done_cards_obj(days, "open")

    print("Closing cards from", data_inicio, "to", data_fim)
    for card in done_cards:
        print(card, "closed")
        text = " **Automation: Closing cards**" + "\n" + "Closed all done cards from " + str(data_inicio) + " to " + str(data_fim)
        card.comment(text)
        cards_number += 1
        card.set_closed(True)

    print("\n" + "Number of closed cards: " + str(cards_number))
