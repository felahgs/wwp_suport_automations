import sys

from trello import TrelloClient
from api import trello
from automation import wwp

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-bye", help="Run all scripts", action="end_of_day")

    args = parser.parse_args()

    print(args.square**2)

