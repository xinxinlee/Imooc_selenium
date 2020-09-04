from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#判断某个网页打开时的标题方法一
title = driver.title
if title == '百度一下，你就知道':
    print('定位成功')
else:
    print('定位失败')

#判断某个网页打开后是不是自己想要的标题方法二
print(EC.title_contains(' 包含可以定位到的标题内容，看打印出来的有没有这个对象来判断是不是对的页面'))

#使用classname 定位的时候前端有时候会返回很多相同classname的元素，这些元素组成一个list 这样就可是使用list的形式来定位自己想要的元素
#比如想要这个list 中的第1个元素
driver.find_elements_by_class_name('类名')[1].click()

#判断某个元素有没有定位到的方式
locator = (By.CLASS_NAME,"controls")#这个参数传给下面的方法用来判断是不是存在某个元素，前面是方法后面是元素名
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))#这个也是返回一个内存中的对象
driver.close()#用来关闭创建的driver实例，否则会打开太多的进程浪费资源
#显示在定位的元素上填入的是什么信息、定位的元素上默认的提示是什么
shop_name = driver.find_element_by_name('shopName')
shop_name.get_attribute('placeholder')#在没有输入任何信息之前取默认值的内容
shop_name.send_keys("要输入的内容")
shop_name.get_attribute('value')#取到上面输入的内容
#比如在测试的过程中需要每次输入不同的用户名，所以需要做一个随机每次都生成不同的用户名，比如邮箱名
i = 0
while i <5:
    a = ''.join(random.sample('1234567890abcdefg',5)) + "@163.com"#使用join这种方式是为了把LIST 转换为字符串
    i += 1

