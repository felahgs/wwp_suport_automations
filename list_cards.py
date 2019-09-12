
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

    param = sys.argv[1]

    trello = trello.TrelloApi()
    my_list = trello.get_list(sys.argv[1])
    print(my_list)

    print("Listing Cards from", my_list.name, '\n')
    for card in my_list.list_cards():
        print(card.name)
