import psycopg2,pymysql,random

class Mysqlop:
	"""docstring for Mysqlop"""
	def __init__(self,database,user,password,host,port=3306):
		self.database = database
		self.user = user
		self.password = password
		self.host = host
		self.port = port

	def open_conntion(self):
		self.conn = pymysql.connect(database = self.database, user = self.user, password = self.password, host = self.host, port = self.port)
		self.cur = self.conn.cursor()

	def close_conntion(self):
		self.cur.close()
		self.conn.close()

	def query_sen(self,sql):
		try:
			self.cur.execute(sql)
			reslut = self.cur.fetchall()
			for select_result in reslut:
				#return select_result
				print(select_result)
		except:
			print("查询语句执行失败。")

	def update_sen(self,sql):
		try:
			self.cur.execute(sql)
			self.conn.commit()
		except:
			print("更新数据失败。")



'''
if __name__ == '__main__':
	database = "xxx"
	user = "xxx"
	password="xxx"
	host="xxx"
	sql = "select * from xxx"
	obj = Mysqlop(database,user,password,host)
	obj.open_conntion()
	obj.query_sen(sql)
'''
