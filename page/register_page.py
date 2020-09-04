from base.find_element import FindElement
#page就是用来完成返回driver.find element by_id 类似这种操作的,现在的主要问题就是把元素定位出来等着后面的handle去sendkey

class RegisterPage:

    def __init__(self,driver):
        self.fd = FindElement(driver)

    def get_shopname_element(self):
        return self.fd.get_element('shop_name')

    def get_username_element(self):
        return self.fd.get_element('user_name')

    def get_password_element(self):
        return self.fd.get_element('pass_word')

    def get_code_element(self):
        return self.fd.get_element('code')

    def get_button_element(self):
        return self.fd.get_element('login_button')

    def get_code_erroe_element(self):
        return self.fd.get_element('code_erroe')

