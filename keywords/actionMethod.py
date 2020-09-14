from selenium import webdriver

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
