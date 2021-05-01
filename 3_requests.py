import requests
res = requests.get("https://google.com")
res.raise_for_status()  #오류가 발생하는 경우 요기서 끝냄
# 위 두줄은 거의 세트

# print("응답코드" : res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")


print("웹 스크래핑을 진행합니다.")

with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)