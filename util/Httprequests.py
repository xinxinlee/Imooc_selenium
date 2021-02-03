import requests
import json

#封装采用json编码格式的请求

class myrequests:

	def __init__(self,url):
		self.url = url
		self.header = {'content-type':'application/json'}

	def myget(self):
		try:
			r = requests.get(self.url)
			return r.text,r.status_code
		except Exception as e:
			print('post请求出错,原因:%s'%e)

	def mypost(self,param):
		try:
			data = json.dumps(param)
			r = requests.post(self.url,data=data,headers=self.header)
			json_response = json.loads(r.text)
			return json_response
		except Exception as e:
			print('post请求出错,原因:%s'%e)