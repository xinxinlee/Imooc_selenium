from business.register_business import RegisterBusiness
from selenium import webdriver
from time import sleep
class FirstCase:
    #把登录的时候的测试用例都按照不同的方法写在下面，只需要调用函数，输入不同的参数来实现测试用例的执行
    #这个部分只要输入测试用例设计的参数，然后判断一下busniess返回的结果是不是与预期相符就可以了
    #要使用busniess的方法在初始化的时需要实例化对应的类，后面的调用方法直接用类操作即可
    def __init__(self,driver):
        self.login = RegisterBusiness(driver)

    # 如果用户名输入错误的时候的用例,直接把参数传给login方法，不需要传给test函数
    def test_login_shopname_error(self):
        res = self.login.login('99999','admin','123456','8888')
        #调用上面的函数后会有返回，使用assert 来判断返回的是不是error
        if res == True:
            print("成功了")
        else:
            print("失败了")

    def test_login_username_error(self):
        self.login.login()

    def test_login_password_error(self):
        self.login.login()

    def test_login_code_error(self):
        self.login.login()

    def test_login_success(self):
        self.login.login()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = '????????'
    driver.get(url)
    driver.maximize_window()
    sleep(3)
    obj = FirstCase(driver)
    obj.test_login_shopname_error()
    driver.close()