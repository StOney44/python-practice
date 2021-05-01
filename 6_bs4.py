import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()  # 혹시 문제 발생시 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")  #res.text 파일을 lxml 파싱을 이용해서 BeautifulSoup 객채로 만듦

print(soup.title)   
print(soup.a)   # soup 객체에서 처음발견되는 a element 출력

print(soup.a.attrs) # attribute 속성
print(soup.a["href"])

# a tag: link

# class가 아래와 같은 a element 찾기
soup.find("a", attrs = {"class":"Nbtn_upload"})
# class가 아래와 같은 어떤 element 찾기
soup.find(attrs = {"class":"Nbtn_upload"})


print(soup.find("li", attrs = {"class" : "rank01"}))

# 위와 같은 방법 a element 찾기
rank1 = soup.find("li", attrs = {"class" : "rank01"})
print(rank1.a)


print(rank1.a.get_text())
# rank1의 다음 element 확인
print(rank1.next_sibling)   # 개행정보가 있는데 프로그래밍에서 애매한부분, 아래의 find 방법으로 해결가능
print(rank1.next_sibling.next_sibling)

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling

rank2 = rank3.previous_sibling.previous_sibling
print(rank2)

# 부모 element로 바로 이동
print(rank1.parent)

# 다음 element 중에 조건에 맞는 테그 탐색 (개행정보등은 생략됨)
rank1.find_next_sibling("li")



rank1.find_next-siblings("li")  # 아래 li 형제"들" 가져옴

# text가 아래와 같은 a tag 불러오기
webtoon = soup.find("a", text="독립일기")
print(webtoon)