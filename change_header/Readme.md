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
K0{M4n1pul4t1ng_c00k13s_1s_qu1t3_3z!!}

# 설명
헤더 변조하는 문제
