import xlutils,xlwt
from xlutils import copy

#使用xlwt
newfile = xlwt.Workbook()
newsheet = newfile.add_sheet('test1',cell_overwrite_ok=True)
newsheet.write(0,0,'aaa')
#newsheet.write(0,0,10)
newfile.save('D:\\Imooc_selenium\\config\\test1.xls')



