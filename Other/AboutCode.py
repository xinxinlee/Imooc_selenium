import json

class Person:
    def __init__(self):
        self.name = "mingming"
        self.age = 18
        self.lists = [4,5,6,"中文字符"]

data = {"dicts": None,"class":None}
dicts = {"name":"mingming","age":21,"lists":[1,2,3,"中文字符"]}
#编码函数
def json_encode():
    #对字典进行编码，会把字典变成字符串
    data_dicts = json.dumps(dicts,indent=4,ensure_ascii=False)#如果此处不加ensure_ascii=False,那这个属性就默认是True,中文在变成字符串后就是\u4e2d\u6587\u5b57\u7b26这样的形式
    #data_dicts = data_dicts.replace('\n', '').replace(' ', '')#由字典编码成字符串后，会有空格和换行等等，可以使用处理字符串的方法对其进行处理
    #print(data_dicts)
    data["dicts"] = data_dicts

    #对类进行编码,会把类中初始方法中的属性都转换成字符串
    data_class = json.dumps(Person(),indent=4,default=lambda obj: obj.__dict__)
    #print(data_class)
    data["class"] = data_class
#解码函数
def json_decode():
    #把字符串重新解成字典
    dicts = json.loads(data['dicts'])
    #print(dicts)
    #把字符串解回字典，无法解回到类
    clazz = json.loads(data["class"])
    #print(clazz)
