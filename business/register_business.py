from handle.register_handle import RegisterHandle
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
        if self.register_h.catch_error():
            print('报错了')
            return True
        else:
            print("没问题")
            return False

