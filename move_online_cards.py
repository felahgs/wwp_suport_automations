# """Move check all the cards from the Waiting Web Fecher list and move the online ones to the Live list"""
# " Date still hard codded"

import sys

from datetime import date

from trello import TrelloClient

from automation import wwp
from api import trello

# Recieves the name of the desired label and the board where it
# is contained. Returns the label object.
def get_label(name, board):
    label_list = board.get_labels()
    for label in label_list:
        if name in label.name: return label
    
if __name__ == "__main__":

    # Initializadtion to be added in a contructor
    # client = TrelloClient(
        # api_key='ca43dd546a8464cf0b7564e0f392dbd1',
        # api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
    # )

    # all_boards = client.list_boards()
    # wls_board = all_boards[1]
    # my_lists = wls_board.list_lists()

    trello = trello.TrelloApi()

    # print(my_lists)
    waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if "Waiting" in bucket.name]
    done_list = [bucket for bucket in trello.my_lists if "Live" in bucket.name]
    print('Checking cards in', waiting_web_fetcher_list)
    print('Checking cards in', done_list)

    # card = trello.get_card('WATCH_US_15471')

    date = date.today().strftime("%d/%m/%Y")

    automation = wwp.Portal()
    automation.login()
    card_number = 1

    for card in waiting_web_fetcher_list[0].list_cards():
        card_name = card.name.split()[0]
        status = automation.get_source_status(card_name)
        # print(card_name, status)
        if (card_number % 5 == 0):
            print('Verificando card ' + str(card_number))
        card_number += 1
        if 'On-line' in status:
            new_name = card_name + ' - Done in ' + date
            print(card_name, status)
            print(new_name)
            card.set_name(new_name)
            card.change_list(done_list[0].id)
            card.change_pos("bottom")
            text = '**Automation: Moving Online Cards**\n' + 'Card ' + card_name + ' moved to ' + done_list[0].name
            card.comment(text)
            print(text, '\n')

    automation.end()
