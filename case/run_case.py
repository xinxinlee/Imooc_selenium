import unittest,HTMLTestRunner

class RunCase(unittest.TestCase):
    def test_case01(self):
        file_path = 'D:\Imooc_selenium\\report\\first_case.html'
        f = open(file_path,'wb')
        case_path = 'D:\Imooc_selenium\case'
        suite = unittest.defaultTestLoader.discover(case_path, pattern='first*.py', top_level_dir=None)
        #unittest.TextTestRunner().run(suite)
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is first report",description="这是第一个测试报告",verbosity=2)
        runner.run(suite)


if __name__ == '__main__':
    unittest.main()
