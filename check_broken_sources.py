
import time, sys, os

from pageobjects.trello import login
from pageobjects.trello import board

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test():
    def __init__(self):
        print("Initializing webdriver\n")
        self.driver = webdriver.Chrome()

    def login_trello(self):
        login_page = login.LoginPage(self.driver)
        login_page.navigate_to_page()
        login_page.try_to_login('fgsouza93@gmail.com', 'Tje3qz%e')

    def fetch_board_sources(self):
        board_page = board.BoardPage(self.driver)
        board_page.navigate_to_page()

    def end(self):
        print("\nClosing browser")
        time.sleep(7)
        self.driver.quit()
        exit(0)


if __name__ == "__main__":

    test = Test()

    # try:
    test.login_trello()
    test.fetch_board_sources()

    # except Exception, e:
    #     exc_type, exc_obj, exc_tb = sys.exc_info()
    #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #     print 'Error running script: ', exc_type, fname, exc_tb.tb_lineno, str(e)

    # finally:
        # test.end()
    test.end()

    
