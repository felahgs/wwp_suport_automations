import sys

from api import trello

from automation import wwp

# Recieves the name of the desired label and the board where it
# is contained. Returns the label object.
def get_label(name, board):
    label_list = board.get_labels()
    # print('label_list', label_list)
    for label in label_list:
        if name in label.name: return label
    
if __name__ == "__main__":

    # Check for file name parameter
    if len(sys.argv) <= 1:
        print('\nMissing Parameter: Enter the file name containing the sources name')
        exit(1)

    # Code logic
    trello = trello.TrelloApi()

    backlog = trello.my_lists[0]

    portal = wwp.Portal()
    portal.login()

    filename = sys.argv[1]
    print('filename', filename)

    with open(filename) as f:
        source_list = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    source_list = [x.strip() for x in source_list] 

    print("\nChecking Sources Status\n")
    for card in source_list:
        print (card, portal.get_source_status(card))

    portal.end()
