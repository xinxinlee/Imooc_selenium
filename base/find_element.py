from util.read_ini import ReadIni
from selenium import webdriver

class FindElement:
    """
    根据不同的配置文件和不同的节点返回对应定位的元素
    """
    def __init__(self,driver,ini_path,node):
        self.driver = driver
        self.element_obj = ReadIni(ini_path,node)

    def get_element(self,key):
        data = self.element_obj.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'class_name':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_id(value)
        except:
            return None