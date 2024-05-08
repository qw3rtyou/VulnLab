# 사용법
- `./start_all.sh`로 모든 도커 활성화할 수 있음  
- 각 디렉토리 별로 실습용 도커가 들어있고 다른 명령어 없이 `./[서버 경로]/start.sh`로 해당 도커 활성화  
- 구현은 완료했지만 노출시키기 싫으면 `start.sh` 대신 `.start.sh`로 통일함  
- `.env`에서 flag 및 포트 설정할 수 있고 편의를 위해 대부분 docker-compose 사용하게 바꿀 예정  


---
# 포트 현황
- 00  sandbox  
- 01  change_header  
- 02  sqli  
- 03  sqli_blind  
- 04  ssti  
- 05  forum_php  
- 06  xss  
- 07  file_upload  
- 08  prototype_pollution  
- 09  file_download  
- 10  dom_clubbering
- 11  base_tag_injection  
- 12  xss_event_handler  
- 13  CRLF injection  
- 14  미정  
- 15  race_condition
- 16
- 17
- 18
- 19
- 20
- 21
- 29 time_based_sqli
- 30 sqli_step1
- 30~35 sqli_filtering_bypass
- 40~   XSS_filtering_bypass


---
# 도커 설명
- change_header - HTTP 헤더 변조 실습
- file_download - PHP File Download 취약점 실습
- file_upload - PHP File Upload 취약점 실습
- forum_php - CRUD 및 다양한 서비스가 구현된 PHP 기반 서버 공격 실습
- kknock_weekly - 유사 CTF 서버(문제는 다른 보안 관련 서비스에서 가져온 것도 있음)
- prototype_pollution - Prototype Pollution 실습
- sandbox - 리눅스 환경 실습
- sqli - SQL Injection 실습
- sqli_blind - SQL Injection 중 Blind SQL Injection 실습
- ssti - SSTI 실습
- xss - XSS 실습
- dom_clubbering - Dom Clubbering 실습 제작 중

---
# 추후 계획
- RFI, LFI
- Race Condition
- OS Command Injection
- eval()


---
# 시간 남으면 할 것
- JWT
- PHP Wrapper
- PHP Type Juggling
- PHP Serialization
- PHP Filter Gadget Chain

- 그리고 pwn, rev, crypto 등등...