import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pageobjects.basepage import BasePage

class ChatPage(BasePage):
    BTN_SEARCH = (By.XPATH, "//body[@class='page page--basic']/div[@class='app-container']/div[@class='noFocusOutline']/div/div/div/div/div/div/div[4]/div[1]/div[1]/div[1]/button[1]")
    INPUT_SEARCH = (By.XPATH, "//input[@placeholder='Pesquisar no Skype']")
    SEARCH_RESULT_GROUP = (By.XPATH, "(//div[contains(@aria-label, 'CHATS EM GRUPO')])/div[2]")
    RECENT_CHAT = (By.XPATH, "//body[@class='page page--basic']/div[@class='app-container']/div[@class='noFocusOutline']/div/div/div/div/div/div/div/div/div/div/div/div[@class='rxCustomScroll rxCustomScrollV active']/div[@class='scrollViewport scrollViewportV']/div/div/div[@id='rx-vlv-2']/div/div[1]")
    INPUT_CHAT = (By.XPATH, "//span")
    TEXT = (By.XPATH, "//div[contains(text(),'Digite aqui')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_chat_with(self, search_name):
        self.wait.until(EC.presence_of_element_located(ChatPage.BTN_SEARCH))
        btn = self.driver.find_element(*ChatPage.BTN_SEARCH)

        self.wait.until(EC.presence_of_element_located(ChatPage.RECENT_CHAT))
        usr = self.driver.find_element(*ChatPage.RECENT_CHAT)

        self.wait.until(EC.presence_of_element_located(ChatPage.INPUT_SEARCH))
        inpt = self.driver.find_element(*ChatPage.INPUT_SEARCH)

        usr.click()
        btn.click()
        inpt.send_keys(search_name)

        time.sleep(4)
        self.wait.until(EC.presence_of_element_located(ChatPage.SEARCH_RESULT_GROUP))
        btn = self.driver.find_element(*ChatPage.SEARCH_RESULT_GROUP)
        btn.click()

    def send_message(self, message):
        self.wait.until(EC.presence_of_element_located(ChatPage.INPUT_CHAT))
        # inpt = self.driver.find_element(*ChatPage.INPUT_CHAT)
        time.sleep(4)
        inpt = self.driver.find_element(*ChatPage.TEXT)
        # inpt = self.driver.find_element(*ChatPage.INPUT_CHAT)
        inpt.click()
        inpt.send_keys('BLABLABLA')
        # inpt.send_keys('BLABLABLA')