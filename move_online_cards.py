# """Move check all the cards from the Waiting Web Fecher list and move the online ones to the Live list"""
# " Date still hard codded"

import sys

from datetime import date

from trello import TrelloClient

from automation import wwp
from api import trello


def get_label(name, board):
    label_list = board.get_labels()
    for label in label_list:
        if name in label.name: return label
    
if __name__ == "__main__":

    number_verifying_card = 1
    number_moved_cards = 0

    trello = trello.TrelloApi()
    
    # print(my_lists)
    fila_desejada = input("Enter column name to parse: ")
    waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if fila_desejada in bucket.name]

    while "Checked" in str(waiting_web_fetcher_list):
        print("*** Attention, the column 'Business Review - Already Checked' can not be parsed. ***" + "\n")
        fila_desejada = input("Enter column name to parse: ")
        waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if fila_desejada in bucket.name]

    done_list = [bucket for bucket in trello.my_lists if "Live" in bucket.name]
    print('Checking cards in', waiting_web_fetcher_list[0].name)
    print('Moving cards to', done_list[0].name)

    # card = trello.get_card('WATCH_US_15471')

    date = date.today().strftime("%d/%m/%Y")

    automation = wwp.Portal()
    automation.login()

    for card in waiting_web_fetcher_list[0].list_cards():
        card_name = card.name.split()[0]
        status = automation.get_source_status(card_name)
        # print(card_name, status)
        if (number_verifying_card % 5 == 0):
            print('Verifying card ' + str(number_verifying_card))
        number_verifying_card += 1
        if 'On-line' in status:
            new_name = card_name + ' - Done in ' + date
            print('\n' + card_name, status)
            print(new_name)
            card.set_name(new_name)
            card.change_list(done_list[0].id)
            card.change_pos("bottom")
            text = '**Automation: Moving Online Cards**\n' + 'Card ' + card_name + ' moved to ' + done_list[0].name
            card.comment(text)
            print(text, '\n')
            number_moved_cards += 1
    
    print('\n\n' + 'Number of moved cards: ' + str(number_moved_cards) + '\n')

    automation.end()
