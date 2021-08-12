from business.register_business import RegisterBusiness
from selenium import webdriver
from time import sleep
import warnings

class Caigoudan:
    def __init__(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get('http://scm.gyl.test.9now.net/login.html')
        self.driver.maximize_window()
        sleep(3)
        self.login = RegisterBusiness(self.driver)

    def caigoudan_login(self):
        self.login.login('203496','admin','123456','8888')


if __name__ == '__main__':
    obj = Caigoudan()
    obj.caigoudan_login()