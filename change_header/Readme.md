# 라업

```python
import requests as req

header = {"User-Agent": "bot"}
cookies = {"cookie": "Sweat cookie~"}
data = {"proxy": "is fun!!"}
url = "http://ssh.knock-on.org:10001/"

res = req.post(headers=header, data=data, cookies=cookies, url=url)

print(res.text)

```

# 플래그
K0{**secret msg**}

# 설명
헤더 변조하는 문제
