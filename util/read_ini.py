import configparser

class ReadIni:
    """
    读取.ini类型的配置文件
    """

    def __init__(self,file_name,node):
        self.cf = self.load_ini(file_name)
        self.node = node

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf

    def get_value(self,element_name):
        element = self.cf.get(self.node,element_name)
        return element

