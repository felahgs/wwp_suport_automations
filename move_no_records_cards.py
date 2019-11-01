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
    #     api_key='ca43dd546a8464cf0b7564e0f392dbd1',
    #     api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
    # )

    # all_boards = client.list_boards()
    # wls_board = all_boards[1]
    # my_lists = wls_board.list_lists()

    number_verifying_card = 1
    number_moved_cards = 0

    trello = trello.TrelloApi()

    date = date.today().strftime("%d/%m/%Y")

    # print(my_lists)
    fila_desejada = input("Enter column name to parse: ")

    no_records_list = [bucket for bucket in trello.my_lists if "Records" in bucket.name]

    if ((fila_desejada == "all") or (fila_desejada == "All")):

        automation = wwp.Portal()
        automation.login()

        print("Moving cards to", no_records_list[0].name)
        waiting_web_fetcher_list = ["Peer Review", "Waiting Web Fetcher", "Daily Review", "Need Review - New Configuration Rejected by Web Fetcher - EXTRACT/Structured", "Needs Review - Crawl/RIP", "Needs Development", "Paused"]
        for queue in waiting_web_fetcher_list:
            queue = [bucket for bucket in trello.my_lists if queue in bucket.name]
            print("Checking cards in", queue[0].name + "\n")
            number_verifying_card = 0
            number_moved_cards = 0
            for card in queue[0].list_cards():
                card_name = card.name.split()[0]
                status = automation.get_source_status(card_name)
                # print(card_name, status)
                if (number_verifying_card % 5 == 0):
                    print("Verifying card " + str(number_verifying_card))
                number_verifying_card += 1
                if "No-New-Records" in status:
                    new_name = card_name + " - Moved in " + date
                    print("\n" + card_name, status)
                    print(new_name)
                    card.set_name(new_name)
                    card.change_list(no_records_list[0].id)
                    card.change_pos("bottom")
                    text = "**Automation: Moving No-New-Records Cards**\n" + "Card " + card_name + " moved to " + no_records_list[0].name
                    card.comment(text)
                    print(text, "\n")
                    number_moved_cards += 1

            print("\n\n" + "Number of moved cards in " + queue[0].name + ": " + str(number_moved_cards) + "\n")

    else:
        waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if fila_desejada in bucket.name]

        while "Checked" or "NMedia" or "Records" in str(waiting_web_fetcher_list):
            if str(waiting_web_fetcher_list) == "Checked":
                print("*** Attention, the column 'Business Review - Already Checked' can not be parsed. ***" + "\n")
            else:
                print("*** Attention, the column 'NMedia - No New Records' can not be parsed. ***" + "\n")
            fila_desejada = input("Enter column name to parse: ")
            waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if fila_desejada in bucket.name]

        print("Checking cards in", waiting_web_fetcher_list[0].name)
        print("Moving cards to", no_records_list[0].name)

        # card = trello.get_card("MEDIA_KH_8409")

        automation = wwp.Portal()
        automation.login()

        for card in waiting_web_fetcher_list[0].list_cards():
            card_name = card.name.split()[0]
            status = automation.get_source_status(card_name)
            # print(card_name, status)
            if (number_verifying_card % 5 == 0):
                print("Verifying card " + str(number_verifying_card))
            number_verifying_card += 1
            if "No-New-Records" in status:
                new_name = card_name + " - Moved in " + date
                print("\n" + card_name, status)
                print(new_name)
                card.set_name(new_name)
                card.change_list(no_records_list[0].id)
                card.change_pos("bottom")
                text = "**Automation: Moving No-New-Records Cards**\n" + "Card " + card_name + " moved to " + no_records_list[0].name
                card.comment(text)
                print(text, "\n")
                number_moved_cards += 1
    
        print("\n\n" + "Number of moved cards: " + str(number_moved_cards) + "\n")
			
    automation.end()
