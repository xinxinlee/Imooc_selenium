from pandas import DataFrame

data={'name':['张三','李四','王五'],'age':[11,12,13],'sex':['男','女','男']}
df=DataFrame(data)
df.to_excel('D:\\Imooc_selenium\\config\\write_sheet.xlsx')
