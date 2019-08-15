from trello import TrelloClient

client = TrelloClient(
    api_key='ca43dd546a8464cf0b7564e0f392dbd1',
    api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
)

all_boards = client.list_boards()
last_board = all_boards[-1]
print('last board', last_board.name)
print('all boards', all_boards)