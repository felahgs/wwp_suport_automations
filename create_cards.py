import sys

from trello import TrelloClient

from api import trello

# Recieves the name of the desired label and the board where it
# is contained. Returns the label object.
def get_label(name, board):
    label_list = board.get_labels()
    # print('label_list', label_list)
    for label in label_list:
        if name in label.name: return label
    
if __name__ == "__main__":

    # Initializadtion to be added in a contructor
    client = TrelloClient(
        api_key='ca43dd546a8464cf0b7564e0f392dbd1',
        api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
    )


    # Code logic
    trello = trello.TrelloApi()

    member = trello.get_member('Felipe')
    members = []
    members.append(member)

    labels = []
    backlog = trello.my_lists[0]

    labels.append(get_label('LOW', trello.wls_board))
    labels.append(get_label('OPS-FAIL', trello.wls_board))
    labels.append(get_label('Project NMEDIA', trello.wls_board))

    all_cards = []
    all_cards = trello.get_all_cards()

    if len(sys.argv) <= 1:
        print('\nMissing Parameter: Enter the file name containing the sources name')
        exit(1)

    filename = sys.argv[1]
    print('filename', filename)

    with open(filename) as f:
        source_list = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    source_list = [x.strip() for x in source_list] 
  
    print("\nCreating new cards..\n")
    for source in source_list:
        if source in all_cards:
            print('Card already in the board:', source)
        else:
            print('Creating card for source:', source)
            backlog.add_card(source, position=1, labels=labels, assign=members)
