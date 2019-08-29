from trello import TrelloClient


client = TrelloClient(
    api_key='ca43dd546a8464cf0b7564e0f392dbd1',
    api_secret='dcda54138ad468433de04f0d422a4407e5dbfb84dad0198347c01bdab40dcde0',
)

all_boards = client.list_boards()
last_board = all_boards[-1]
wls_board = all_boards[1]
my_lists = wls_board.list_lists()


# for list in my_lists:
#     if "Live" in list.name: live_list = list

# for cards in live_list.list_cards():
#     print(cards.name)

for list in my_lists:
    for card in list.list_cards(card_filter='all'):
        if "BD_775" in card.name: 
            print(card.name)
            out = card.plugin_data
            print(out)


# print(live_list.list_cards())

# my_object = live_list

# object_methods = [method_name for method_name in dir(my_object)
#                   if callable(getattr(my_object, method_name))]
# print(object_methods)
# print (' ')

# from pprint import pprint
# pprint(vars(my_object)) 

