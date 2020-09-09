import ddt,unittest

@ddt.ddt
class DateTest(unittest.TestCase):
    def setUp(self) -> None:
        print("这是setup")
    def tearDown(self) -> None:
        print("这是teardown")

    #@ddt.data(['1','2'],['3','4'],['5','6'])
    @ddt.data([1, 2], [3, 4], [5, 6])
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)

if __name__ == '__main__':
    unittest.main()


