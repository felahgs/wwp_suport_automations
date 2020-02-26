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

    # backlog = trello.my_lists[0]

    filename = sys.argv[1]
    print('filename', filename)

    with open(filename) as f:
        source_list = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    source_list = [x.strip() for x in source_list] 

    fila = input("Digite a fila de destino: ")
    fila_destino = [bucket for bucket in trello.my_lists if fila in bucket.name]

    print("\nMovendo cards\n")

    automation = wwp.Portal()
    automation.login()
    
    for card in source_list:
        # card_name = card.name.split()[0]
        card.change_list(fila_destino[0].id)
        card.change_pos("top")
        text = '**Automation: Moving Cards**\n' + 'Card ' ' moved to ' + fila_destino[0].name
        description = 'Needs Developlment. Show more button'
        card.set_description(description)
        card.comment(text)
        print(text, '\n')
    
    print('\n\n' + 'Cards movidos' + '\n')
			
    automation.end()

