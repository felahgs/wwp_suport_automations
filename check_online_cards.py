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


    fila_desejada = input("\n" + "Enter the column name to verify the cards status: ")

    while (fila_desejada == ""):
        print ("\n" + "Please enter a column name.")
        fila_desejada = input("\n" + "Enter the column name to verify the cards status: ")

    waiting_web_fetcher_list = [bucket for bucket in trello.my_lists if fila_desejada in bucket.name]
    print("\n" + "Checking cards in", waiting_web_fetcher_list[0].name)


    automation = wwp.Portal()
    automation.login()
    for card in waiting_web_fetcher_list[0].list_cards():
        card_name = card.name.split()[0]
        print(card_name, automation.get_source_status(card_name))
        # print(automation.get_source_status(card_name))

    automation.end()

