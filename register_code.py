from selenium import webdriver
import time

driver = webdriver.Chrome()
def driver_init():
    driver.get("??????")
    driver.maximize_window()
    time.sleep(5)

def get_element_byid(id):
    element = driver.find_element_by_id(id)
    return element

def get_element_byname(name):
    element = driver.find_element_by_name(name)
    return element

def get_element_byxpath(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

def get_range_user():
    a = ''.join(random.sample('1234567890abcdefg', 5))
    return a

if __name__ == '__main__':
    driver_init()
    shopname = get_element_byname('shopName')
    shopname.send_keys('99999')
    username = get_element_byname("userName")
    username.send_keys("admin")
    password = get_element_byname("password")
    password.send_keys('123456')
    code = get_element_byname('authcode')
    code.send_keys("8888")
    driver.close()
    
