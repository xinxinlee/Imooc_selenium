from selenium import webdriver
from base.find_element import FindElement
from time import sleep

class ActionMethod:
    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self,browser):
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        return driver

    def get_url(self,url):
        self.driver.get(url)

    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    def element_send_keys(self,key,value):
        element = self.get_element(key)
        element.send_keys(value)

    def element_click(self,key):
        element = self.get_element(key)
        element.click()

    def sleep_time(self,s):
        sleep(s)

    def close_browser(self):
        self.driver.close()






