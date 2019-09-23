
import time, sys, os, re, datetime

from pageobjects.trello import login
from pageobjects.trello import board
from pageobjects.wwp import login
from pageobjects.wwp import source

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from api import trello

from automation import wwp

from utils import date

# class dateChecker():
#     def daterange(self, date1, date2):
#         for n in range(int ((date2 - date1).days)+1):
#             yield date1 + datetime.timedelta(n)

#     def get_days_beetween(self, date1, date2):
#         days = []
#         for dt in self.daterange(date1, date2):
#             # print(dt.strftime("%d/%m/%y"))
#             days.append(dt.strftime("%d/%m/%Y"))
#         return days

#     def convert_to_date(self, date):
#         dd = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%d'))
#         mm = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m'))
#         yyyy = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%Y'))
#         return datetime.date(yyyy,mm,dd)


if __name__ == "__main__":
    
    my_date = date.dateChecker()
    start = my_date.convert_to_date("01/06/2019")
    end = my_date.convert_to_date("10/06/2019")
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
