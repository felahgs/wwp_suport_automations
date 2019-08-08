
import unittest
import time

from pageobjects.trello import login

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_check_groups_list(self):
        print("testing")
	login_page = login.LoginPage(self.driver)
        login_page.navigate_to_page()
        login_page.try_to_login('fgsouza93@gmail.com', 'Tje3qz%e')


    def tearDown(self):
        time.sleep(7)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)
