import requests

url = " http://nadocoding.tistory.com"
# 접속하는 uger agent를 바꿔서 일반 사람이 접속하는 것처럼 설정 (서버 과부화 혹은 데이터 악용 등의 이유로 uger가 사람이 아닌 프로그램이라고 판단되는 경우 제한되는 업무도 있음)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

res = requests.get(url, headers = headers)  #위 지정한 헤더로 request 요청을 실행

#res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
