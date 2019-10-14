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
    print('**Renaming cards from ', list, 'Done in 02/04/2019')
    for card in list.list_cards():
        if "- Done in 02/04/2019'" in card.name:
            old_name = card.name 
            new_name = card.name.replace(' - Done in 02/10/2019', ' - Done in 02/04/2019')
            # card.set_name (new_name)
            text = '**Automation: Renaming cards**\n' + 'Old name: ' + old_name + '\nNew name: ' + new_name
            # card.comment(text)
            print(text, '\n')
            # print('new name =', card.name.replace('- n', '- o'), '\n')


