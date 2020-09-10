import configparser

class ReadIni:

    def __init__(self,file_name,node):
        self.cf = self.load_ini(file_name)
        self.node = node

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    def get_value(self,element_name):
        element = self.cf.get(self.node,element_name)
        return element

if __name__ == '__main__':
    file_name = ''
    read_obj = ReadIni('D:\\Imooc_selenium\\config\\LocalElement.ini','RegisterElement')
    a = read_obj.get_value('shop_name')
    print(a)


