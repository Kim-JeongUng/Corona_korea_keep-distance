import requests
from bs4 import BeautifulSoup
import pandas as pd

import jenan
import coronaNow
# 웹 크롤링
webpage = requests.get("http://ncov.mohw.go.kr/regSocdisBoardView.do?brdId=6&brdGubun=68&ncvContSeq=495")
soup = BeautifulSoup(webpage.content, "html.parser")

# 행정구역 엑셀
df = pd.read_excel('C:/Users/USER/PycharmProjects/Corona_korea_keep-distance/행정구역.xlsx')

print(soup.find(attrs={'class': 'timetable'}).text + " 사회적 거리두기 단계\n\n")

area_level = [[], [], [], []]

target = 4


def junsu(level):
    print("\n", level, "단계 준수 수칙")

    if level == 1:
        print("사적 모임 가능")
        print("유흥시설 운영시간 제한 없음")
        print("식당,카페 운영시간 제한 없음")
        print("코인노래방 운영시간 제한 없음")
        print("PC방 제한없음")
        print("헬스장 제한없음")

    if level == 2:
        print("사적 모임 가능")
        print("유흥시설 24시 이후 운영제한")
        print("식당,카페 24시 이후 포장 배달만 허용")
        print("코인노래방 24시 이후 운영제한")
        print("PC방 제한없음")
        print("헬스장 제한없음")

    if level == 3:
        print("4인까지 모임가능")
        print("유흥시설 22시 이후 운영제한")
        print("식당,카페 22시 이후 포장 배달만 허용")
        print("코인노래방 22시 이후 운영제한")
        print("PC방 제한없음")
        print("헬스장 제한없음")

    if level == 4:
        print("18시 이후 2명까지 모임가능, 18시 이전 4인까지 모임가능")
        print("유흥시설 집합금지")
        print("식당,카페 22시 이후 포장 배달만 허용")
        print("코인노래방 22시 이후 운영제한")
        print("PC방 22시 이후 운영제한")
        print("헬스장 22시 이후 운영제한")
    print()


# 전체지역 코로나 단계 출력
for descript in soup.find_all("p", "rssd_descript"):
    print(target, "단계")

    area_level[target - 1] = descript.text
    print(area_level[target - 1])

    target -= 1
    if target < 1:
        break

while 1:
    print("\n지역을 입력하세요 : ")
    my_area = input()

    do = df['시도명'].loc[df['시군구명'].str.contains(my_area) == True]
    dov = ""

    for val in do:
        dov = val

    for i in range(0, len(area_level)):
        if area_level[i].find("(" + my_area) != -1:
            print(my_area, "지역은", i + 1, "단계 입니다.")
            junsu(i + 1)
            jenan.jenan_area(my_area)
            coronaNow.CovidArea(my_area)
            break

        elif area_level[i].find(", " + my_area) != -1:
            print(my_area, "지역은", i + 1, "단계 입니다.")
            junsu(i + 1)
            jenan.jenan_area(my_area)
            coronaNow.CovidArea(my_area)
            break

        elif i == len(area_level) - 1:
            if dov == "":
                print("데이터가 없습니다. 다시 검색하세요")
                break
            else:
                print(my_area, "지역의 상급 행정구역", dov, "으로 검색됩니다. ")
                i = 0
                my_area = dov

                for j in range(0, len(area_level)):
                    if area_level[j].find("(" + my_area) != -1:
                        print(my_area, "지역은", j + 1, "단계 입니다.")
                        junsu(j + 1)
                        jenan.jenan_area(my_area)
                        coronaNow.CovidArea(my_area)
                        break

                    elif area_level[j].find(", " + my_area) != -1:
                        print(my_area, "지역은", j + 1, "단계 입니다.")
                        junsu(j + 1)
                        jenan.jenan_area(my_area)
                        coronaNow.CovidArea(my_area)
                        break
