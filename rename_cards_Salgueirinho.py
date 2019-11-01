import sys

from trello import TrelloClient

from automation import wwp
from api import trello

# client = TrelloClient(
#     api_key='ca43dd546a8464cf0b7564e0f392dbd1',
#     api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
# )

trello = trello.TrelloApi()

# all_boards = client.list_boards()
# wls_board = all_boards[1]
# my_lists = wls_board.list_lists()

my_lists = [bucket for bucket in trello.my_lists if "Live" in bucket.name]


# Search for every card on the board that contins 'Source' and remove from their name

# quewe = my_lists[0]
# print('my_list', quewe, '\n')
print('**RENAMING CARDS. REMOVING \'Source\' FROM THE CARDS NAMES**\n')

if len(sys.argv) <= 1:
    print('\nMissing Parameter: Enter the file name containing the sources name')
    exit(1)

filename = sys.argv[1]
print('filename', filename)

with open(filename) as f:
    source_list = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
source_list = [x.strip() for x in source_list]

for list in my_lists:
    print('**Renaming cards from ', list, '**\n')
    for card in list.source_list:
        if "18/10/2019" in card.name:
            old_name = card.name 
            new_name = card.name.replace('18/10/2019', '21/10/2019')
            card.set_name (new_name)
            text = '**Automation: Renaming cards**\n' + 'Old name: ' + old_name + '\nNew name: ' + new_name
            card.comment(text)
            print(text, '\n')
            # print('new name =', card.name.replace('- n', '- o'), '\n')


