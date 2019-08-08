
import time

from pageobjects.trello import login

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test():
    def __init__(self):
        print("Initializing webdriver")
        self.driver = webdriver.Chrome()

    def test_check_groups_list(self):
        login_page = login.LoginPage(self.driver)
        login_page.navigate_to_page()
        login_page.try_to_login('fgsouza93@gmail.com', 'Tje3qz%e')


    def end(self):
        print("Closing browser")
        time.sleep(7)
        self.driver.quit()
        exit(0)

if __name__ == "__main__":
    test1 = Test()
    test1.test_check_groups_list()
    test1.end()
    exit(0)
