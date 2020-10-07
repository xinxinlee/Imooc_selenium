import mock

class Test01:
    id = 1
    no = 2
    def fuc01(self):
        return self.id
if __name__ == '__main__':
    obj = Test01()
    print(obj.fuc01())