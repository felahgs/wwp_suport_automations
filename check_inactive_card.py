import sys

from api import trello

from automation import wwp


# Recieves the name of the desired label and the board where it
# is contained. Returns the label object.
def get_label(name, board):
    label_list = board.get_labels()
    for label in label_list:
        if name in label.name: return label
    
if __name__ == "__main__":

    trello = trello.TrelloApi()

    waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if "Waiting" in bucket.name]
    print('Checking cards in', waiting_web_fetcher_list)


    automation = wwp.Portal()
    automation.login()
    # card_number = 1
    
    for card in waiting_web_fetcher_list[0].list_cards():
        # print('verificando card ' + str(card_number))
        # card_number += 1
        card_name = card.name.split()[0]
        status = automation.get_source_status(card_name)
        if 'Inactive' in status:
            print('\n' + card_name, automation.get_source_status(card_name) + '\n')
            # print(automation.get_source_status(card_name))

    automation.end()

