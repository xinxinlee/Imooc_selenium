from util.read_ini import ReadIni
from selenium import webdriver

class FindElement:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        element_obj = ReadIni('D:\Imooc_selenium\config\LocalElement.ini','RegisterElement')
        data = element_obj.get_value(key)
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
            self.driver.save_screenshot('D:\Imooc_selenium\Image\\%s.png' %value)
            return None


