import unittest

class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('前置')
    @classmethod
    def tearDownClass(cls):
        print('后置')
    def test_first01(self):
        print("test01")

    def test_first02(self):
        print('test02')

if __name__ == '__main__':
    unittest.main()