import unittest

class FirstCase01(unittest.TestCase):
    def setUp(self):
        print('前置')

    def tearDown(self):
        print('后置')

    def test_first01(self):
        print(self._testMethodName)

    @unittest.skip('不执行02这一条')
    def test_first02(self):
        print('test02')

if __name__ == '__main__':
    case_path = 'D:\Imooc_selenium\case'
    suite = unittest.defaultTestLoader.discover(case_path, pattern='unittest*.py', top_level_dir=None)
    unittest.TextTestRunner().run(suite)
