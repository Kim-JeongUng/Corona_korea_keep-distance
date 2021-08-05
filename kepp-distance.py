import requests
from bs4 import BeautifulSoup
import re

webpage = requests.get("http://ncov.mohw.go.kr/regSocdisBoardView.do?brdId=6&brdGubun=68&ncvContSeq=495")
soup = BeautifulSoup(webpage.content, "html.parser")

print(soup.find(attrs={'class': 'timetable'}).text + " 사회적 거리두기 단계\n\n")

level=[[],[],[],[]]

#전체 출력
target = 4
for descript in soup.find_all("p","rssd_descript"):
    print(target,"단계")

    level[target-1]=descript.text
    print(level[target-1])

    target-=1
    if target < 1 :
        break;


# 지역별
while(1):
    print("지역을 입력하세요 : ")
    my_area = input()

    target = 4


    for i in range(0,len(level)):
        if level[i].find("("+my_area) != -1:
            print(my_area,"지역은",i+1,"단계 입니다.")
            print(i+1,"단계 준수 수칙")
            break;

        elif level[i].find(", "+my_area) != -1:
            print(my_area, "지역은", i + 1, "단계 입니다.")
            print(i + 1, "단계 준수 수칙")
            break;

        elif i == len(level)-1:
            print("데이터가 없습니다. 행정구역 \'도\'로 다시 검색하세요")



