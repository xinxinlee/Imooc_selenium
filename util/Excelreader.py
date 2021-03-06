import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from xlutils.copy import copy

'''
xlrd中单元格的数据类型
数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换
成我们想要的数据类型
0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
'''

class ExcelDate:

	def __init__(self,data_path,sheetname):

		self.data_path = data_path
		self.sheetname = sheetname
		self.data = xlrd.open_workbook(self.data_path)
		self.table = self.data.sheet_by_name(self.sheetname)
		self.nrows = self.table.nrows
		self.ncols = self.table.ncols
		self.keys = self.table.row_values(0)

	def readExcel(self):
		try:
			datas = []
			for row in range(1,self.nrows):
				sheet_data = {}
				for col in range(self.ncols):
					c_type = self.table.cell(row,col).ctype
					c_cell = self.table.cell(row,col).value
					if c_type == 2 and c_cell % 1 == 0:
						c_cell = int(c_cell)
					elif c_type == 3:
						date = datetime(*(xldate_as_tuple(self.table.cell(row, col).value, 0)))
						c_cell = date.strftime('%Y/%d/%m %H:%M:%S')
					elif c_type == 4:
						c_cell = True if c_cell == 1 else False
					sheet_data[self.keys[col]] = c_cell
				datas.append(sheet_data)
			return datas

		except Exception as e:
			print('获取测试用例数据失败，原因：%s'%e)
#返回的形式是[[],[],[],...]
	def for_ddtlist(self):
		list_result = []
		for i in range(1,self.nrows):
			list1 = []
			for j in range(self.ncols):
				cell = self.table.cell(i, j).value
				if type(cell) == float:
					cell = int(cell)
				list1.append(cell)
			list_result.append(list1)
		return list_result

	def get_lines(self):
		rows = self.table.nrows
		if rows>=1:
			return rows
		return None

	def get_col_value(self,row,col):
		if self.get_lines()> row:
			data = self.table.cell(row,col).value
			if type(data) == float:
				data = int(data)
			return str(data).strip()
		return None

	def write_value(self,row,value):
		read_value = self.data
		write_data = copy(read_value)
		write_data.get_sheet(0).write(row,7,value)
		write_data.save('D:\\Imooc_selenium\\config\\keywords.xls')


if __name__ == "__main__":
	data_path = "D:\\Imooc_selenium\\config\\case.xlsx"
	sheetname = "logincase"
	get_data = ExcelDate(data_path,sheetname)
	#datas = get_data.for_ddtlist()
	# datas = get_data.get_col_value(1,3)
	#datas = get_data.write_value(7,'test')
	#datas = get_data.get_lines()
	# print(datas)
	# print(type(datas))
	# print(get_data.nrows)
	# print(get_data.ncols)
	data_list = []
	for i in range(1,get_data.nrows):
		data = get_data.get_col_value(i,1)
		data_list.append(data)
	print(data_list)

