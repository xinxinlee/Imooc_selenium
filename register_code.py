from selenium import webdriver
import time

driver = webdriver.Chrome()
def driver_init():
    driver.get("http://scm.gyl.test.9now.net/login.html")
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

def get_element_byclassname(classname):
    element = driver.find_element_by_class_name(classname)
    return element

def get_range_user():
    a = ''.join(random.sample('1234567890abcdefg', 5))
    return a

if __name__ == '__main__':
    driver_init()
    shopname = get_element_byname('shopName')
    shopname.send_keys('')
    username = get_element_byname("userName")
    username.send_keys("")
    password = get_element_byname("password")
    password.send_keys('')
    code = get_element_byname('authcode')
    code.send_keys("")
    get_element_byxpath('/html/body/div[2]/div/div/div/form/button').click()
    time.sleep(1)
    alert_text = get_element_byclassname('ant-message')
    text = alert_text.text
    print(text)

    driver.close()
    
