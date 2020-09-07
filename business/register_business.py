from handle.register_handle import RegisterHandle
import time
#业务层需要构造一个case层只需要输入用例可以直接返回结果的方法，其中增需要增加判断来返回参数不同时的各种返回
#比如登录时输入商户名错误页面会返回错误提示可以在输入用户名后来一个if 语句，如果错误提示元素被定位到则返回对应的提示供
#供case 的assert 判断用例执行是否成功
#这里调用了handle层的方法，主要就是操作页面元素后send_keys 这个步骤，这里不需要driver
class RegisterBusiness:

    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self,shopname,username,password,code):
        self.register_h.send_shopname(shopname)
        self.register_h.send_username(username)
        self.register_h.send_password(password)
        self.register_h.seng_code(code)
        self.register_h.click_button()

    def login(self,shopname,username,password,code):
        self.user_base(shopname,username,password,code)
        time.sleep(1)
        if self.register_h.alert_tips().text == '登录成功':
            print('商户名用户名密码验证码正确，验证成功。')
        elif self.register_h.alert_tips().text == '登录失败，请检查商户名，账号，密码，验证码是否正确!':
            print(('商户名用户名密码验证码其中有一项不正确，验证成功。'))
        elif self.register_h.alert_tips().text == '请输入您的商户ID':
            print('未输入商户名，验证成功。')
        else:
            print('其他错误提示。')