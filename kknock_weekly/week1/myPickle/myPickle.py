import pickle
import zlib
import base64
from datetime import datetime

import flag

class Dic:
	def __init__(self, dic):
		self.username = dic["username"]
		self.password = dic["password"]
		self.is_admin = dic["is_admin"]
		self.date = dic["date"]

	def f(self):
		if(self.is_admin):
			print("oh.. hello admin, good to you.")
			flag.flag()
		else:
			print("\nhello " + self.username + ", welcome to k.knock.")
			print("============== profile ==============")
			print("Username : " + self.username)
			print("Password : " + self.password)
			print("Generate date : " + self.date + "\n")

def menu():
	print("1. Generate key")
	print("2. Authenticate")
	print("3. Exit")

while(True):
	print("hello guys, what do you want?")
	menu()
	try:
		num = int(input(">> "))
	except:
		exit(0)
		
	if(num == 1):

		username = input("Username : ")
		password = input("Password : ")
		date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

		dic = {"username":username, "password":password, "is_admin":False, "date":date}
		key = Dic(dic)

		key = pickle.dumps(key)
		key = zlib.compress(key)
		key = base64.b64encode(key)
			
		print("key : " + key.decode() + "\n")

	elif(num == 2):
		print("Are you admin? submit your key.")
		try:
			userInput = input(">> ").encode()
			userInput = base64.b64decode(userInput)
			userInput = zlib.decompress(userInput)
			userInput = pickle.loads(userInput)
		except:
			print("invalid key.\n")
			continue
		userInput.f()

	elif(num == 3):
		print("bye.")
		exit(0)

	else:
		print("choose 1~3")


