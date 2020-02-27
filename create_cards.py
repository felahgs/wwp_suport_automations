import sys
from trello import TrelloClient
from api import trello
from automation import wwp

if __name__ == "__main__":

    trello = trello.TrelloApi()

    # member = trello.get_member('Felipe')
    members = []
    # members.append(member)

    labels = []
    backlog = trello.get_list("Waiting")

    automation = wwp.Portal()
    automation.login()

    # Add a label to the card, the label should exist in the board. The first label that contains
    # the selected string will be added.

    # labels.append(trello.get_label('HIGH'))
    # labels.append(trello.get_label('QA-FAIL'))
    # labels.append(trello.get_label('OPS-FAIL'))
    # labels.append(trello.get_label('Project NMEDIA'))

    needs_label = input("Want to add some label to all cards? (Y/N) ")
    while needs_label == "Y":
        label = input("Enter the exact name of the label: " + "\n\n")
        labels.append(trello.get_label(label))
        needs_label = input("\n" + "Want to add some more label to all cards? (Y/N) ")

    
    needs_member = input("\n\n" + "Want to add some member to all cards? (Y/N) ")
    if needs_member == "Y":
        member = input("Enter the exact name of the member: " + "\n\n")
        members.append(trello.get_member(member))

    all_cards = []
    all_cards_names = []
    get_cards = trello.get_all_open_cards()
    for card in get_cards:
        all_cards_names.append(card.name)
        

    if len(sys.argv) <= 1:
        print("\n" + "Missing Parameter: Enter the file name containing the sources name")
        exit(1)
    filename = sys.argv[1]
    print("filename", filename)

    with open(filename) as f:
        source_list = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    source_list = [x.strip() for x in source_list] 
  
    print("\n" + "Creating new cards.." + "\n")

    combined = "\t".join(all_cards_names)

    for source in source_list:
        if source in combined:
            print("Card already in the board:", source)
        else:
            priority = automation.get_source_priority(source)
            labels.append(trello.get_label(priority))
            print("Creating card for source:", source, " priority: ", priority)
            backlog.add_card(source, position="bottom", labels=labels, assign=members)
            labels.pop()