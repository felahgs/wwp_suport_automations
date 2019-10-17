import sys

from api import trello

# Recieves the name of the desired label and the board where it
# is contained. Returns the label object.
def get_label(name, board):
    label_list = board.get_labels()
    for label in label_list:
        if name in label.name: return label
    
if __name__ == "__main__":

    trello = trello.TrelloApi()

    labels = []
    backlog = trello.my_lists[0]

    # Code logic
    labels.append(get_label('QA-FAIL', trello.wls_board))
    labels.append(get_label('LOW', trello.wls_board))
  
    if len(sys.argv) > 1: 
	    print('arg', sys.argv[1])
    else:
	    print('Execute the script following the number of cards to be created!')
	    exit(1)

    print(labels)
    for i in range(int(sys.argv[1])):
        print(i + 1, 'Card' if i==0 else 'Cards', 'created')
        backlog.add_card('Source', position=1, labels=labels)
