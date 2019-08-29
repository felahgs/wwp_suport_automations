from trello import TrelloClient


client = TrelloClient(
    api_key='ca43dd546a8464cf0b7564e0f392dbd1',
    api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
)

all_boards = client.list_boards()
last_board = all_boards[-1]
wls_board = all_boards[1]
my_lists = wls_board.list_lists()


# Search for every card on the board that contins 'Source' and remove from their name

# quewe = my_lists[0]
# print('my_list', quewe, '\n')
print('**RENAMING CARDS. REMOVING \'Source\' FROM THE CARDS NAMES**\n')

for list in my_lists:
    print('**Renaming cards from ', list, '**\n')
    for card in list.list_cards(card_filter='all'):
        if "Source" in card.name: 
            print('old name =', card.name)
            card.set_name (card.name.replace('Source', ''))
            print('new name =', card.name, '\n')
    print('\n')

