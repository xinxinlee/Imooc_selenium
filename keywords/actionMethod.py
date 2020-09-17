from selenium import webdriver
from base.find_element import FindElement
from time import sleep
#这个类是用来封装各种操作的，如打开关闭浏览器，获取元素，操作元素等一下动作
class ActionMethod:
    def __init__(self,browser):
        self.driver = self.get_driver(browser)
        self.driver.maximize_window()


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


if __name__ == '__main__':
    obj = ActionMethod('chrome')
    obj.get_url('http://scm.gyl.test.9now.net/login.html')
    obj.sleep_time(3)
    obj.element_send_keys('shop_name','99999')
    obj.element_send_keys('user_name', 'admin')
    obj.element_send_keys('pass_word', '123456')
    obj.element_send_keys('code', '8888')
    obj.element_click('login_button')
    obj.sleep_time(3)
    obj.close_browser()


