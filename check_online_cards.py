import sys

from trello import TrelloClient

from automation import wwp


# Recieves the name of the desired label and the board where it
# is contained. Returns the label object.
def get_label(name, board):
    label_list = board.get_labels()
    for label in label_list:
        if name in label.name: return label
    
if __name__ == "__main__":

    # Initializadtion to be added in a contructor
    client = TrelloClient(
        api_key='ca43dd546a8464cf0b7564e0f392dbd1',
        api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
    )

    all_boards = client.list_boards()
    wls_board = all_boards[1]
    my_lists = wls_board.list_lists()

    # print(my_lists)
    in_progress_list = [bucket for bucket in my_lists if "Waiting" in bucket.name]
    print(in_progress_list)


    automation = wwp.Portal()
    automation.login()
    for card in in_progress_list[0].list_cards():
        print(card)
        print(automation.get_source_status(card.name))

    automation.end()

    # labels = []
    # backlog = my_lists[0]

    # # Code logic
    # labels.append(get_label('QA-FAIL', wls_board))
    # labels.append(get_label('LOW', wls_board))
  
    # if len(sys.argv) > 1: 
	#     print('arg', sys.argv[1])
    # else:
	#     print('Execute the script following the number of cards to be created!')
	#     exit(1)

    # print(labels)
    # for i in range(int(sys.argv[1])):
    #     print(i + 1, 'Card' if i==0 else 'Cards', 'created')
    #     backlog.add_card('Source', position=1, labels=labels)
