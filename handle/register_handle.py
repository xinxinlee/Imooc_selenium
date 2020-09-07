from page.register_page import RegisterPage

#主要完成页面定位，等着输入sendkey 这个操作，就是说调用page的定位元素，然后handel 就负责send_key

class RegisterHandle:
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)
    #输入门店名称
    def send_shopname(self,shopname):
        return self.register_p.get_shopname_element().send_keys(shopname)
    #输入用户名
    def send_username(self,username):
        return self.register_p.get_username_element().send_keys(username)
    #输入密码
    def send_password(self,password):
        return self.register_p.get_password_element().send_keys(password)
    #输入验证码
    def seng_code(self,code):
        return self.register_p.get_code_element().send_keys(code)
    #获取提交时错误的弹窗元素

    def click_button(self):
        return self.register_p.get_button_element().click()

    def alert_tips(self):
        return self.register_p.get_alert_tips_element()

