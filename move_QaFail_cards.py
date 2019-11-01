# """Move check all the cards from the Waiting Web Fecher list and move the online ones to the Live list"""
# " Date still hard codded"

import sys

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

    number_verifying_card = 1
    number_moved_cards = 0

    trello = trello.TrelloApi()

    # print(my_lists)
    fila_desejada = input("Enter column name to parse: ")
    waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if fila_desejada in bucket.name]
    # waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if "Waiting" in bucket.name]

    peer_list = [bucket for bucket in trello.my_lists if "Peer" in bucket.name]
    print("Checking cards from", waiting_web_fetcher_list[0].name)
    print("Moving cards to", peer_list[0].name)

    # card = trello.get_card("WATCH_US_15471")

    automation = wwp.Portal()
    automation.login()

    if "Peer" in fila_desejada:
        for card in waiting_web_fetcher_list[0].list_cards():
            card_name = card.name.split()[0]
            status = automation.get_source_status(card_name)
            if (number_verifying_card % 5 == 0):
                print("Verifying card " + str(number_verifying_card))
            number_verifying_card += 1
            # if "WATCH" in card_name:
            if "xPath" in status:
                print("\n" + card_name, status)
                card.change_pos("top")
                number_moved_cards += 1
            if "QA-Fail" in status:
                print("\n" + card_name, status)
                card.change_pos("bottom")
                number_moved_cards += 1
    else:
        for card in waiting_web_fetcher_list[0].list_cards():
            card_name = card.name.split()[0]
            status = automation.get_source_status(card_name)
            # print(card_name, status)
            if (number_verifying_card % 5 == 0):
                print("Verifying card " + str(number_verifying_card))
            number_verifying_card += 1
            if "WATCH" in card_name:
                if "QA-Fail" in status:
                    print("\n" + card_name, status)
                    card.change_list(peer_list[0].id)
                    card.change_pos("bottom")
                    text = "**Automation: Moving 'QA-Fail' Cards**\n" + "Card " + card_name + " moved to " + peer_list[0].name
                    card.comment(text)
                    print(text, "\n")
                    number_moved_cards += 1
                if "xPath" in status:
                    print("\n" + card_name, status)
                    card.change_list(peer_list[0].id)
                    card.change_pos("top")
                    text = "**Automation: Moving 'xPath Error' Cards**\n" + "Card " + card_name + " moved to " + peer_list[0].name
                    card.comment(text)
                    print(text, "\n")
                    number_moved_cards += 1

    
    print("\n\n" + "Number of moved cards: " + str(number_moved_cards) + "\n")

    automation.end()
