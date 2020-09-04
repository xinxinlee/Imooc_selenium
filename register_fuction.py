from selenium import webdriver
import time
from base.find_element import FindElement

class RegisterFunction:
    def __init__(self,url):
        self.driver = self.get_driver(url)

    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    def driver_close(self):
        self.driver.close()


if __name__ == '__main__':
    url = 'http://scm.gyl.test.9now.net/login.html'
    obj = RegisterFunction(url)
    obj.send_user_info('shop_name','99999')
    obj.send_user_info('user_name','admin')
    obj.send_user_info('pass_word','123456')
    obj.send_user_info('code','8888')
    time.sleep(3)
    obj.get_user_element('login_button').click()
    #获取弹窗元素
    err_code = obj.get_user_element('code_erroe')
    if err_code == None:
        print("成功了")
    else:
        obj.driver.save_screenshot("D:\Imooc_selenium\Image\\test2.png")
    time.sleep(5)
    obj.driver_close()







