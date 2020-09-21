import ddt,unittest,warnings
from business.register_business import RegisterBusiness
from selenium import webdriver
from time import sleep
from util.Excelreader import ExcelDate
from log.user_log import UserLog

data_path = "D:\\Imooc_selenium\\config\\case.xlsx"
sheetname = "logincase"
exc = ExcelDate(data_path,sheetname)
data = exc.for_ddtlist()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get('http://scm.gyl.test.9now.net/login.html')
        self.driver.maximize_window()
        self.logger.info("chrome is openning")
        sleep(3)
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        #截图处理代码每次用例执行完毕后会在收尾处进行截图
        case_name = self._testMethodName#用例的名字
        self.driver.save_screenshot('D:\\Imooc_selenium\\Image\\%s.png' % case_name)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    @ddt.data(*data)
    def test_login(self,data):
        shopname,username,password,code = data
        res = self.login.login(shopname,username,password,code)
        return res
