# 거리두기 단계 및 준수 수칙 크롤링

import requests
from bs4 import BeautifulSoup

# 거리두기 단계 웹 크롤링
webpage = requests.get("http://ncov.mohw.go.kr/regSocdisBoardView.do?brdId=6&brdGubun=68&ncvContSeq=495")
soup = BeautifulSoup(webpage.content, "html.parser")

area_level = [[], [], [], []]


# 거리두기 단계 별 방역수칙 웹 크롤링
KeepDistanceLevel = requests.get("http://ncov.mohw.go.kr/socdisBoardView.do?brdId=6&brdGubun=1")
KeepDistanceLevelSoup = BeautifulSoup(KeepDistanceLevel.content, "html.parser")

Distance = []

# 거리두기단계 준수수칙
def Junsu(level):
    print("\n", level, "단계 준수 수칙")

    if level == 1:
        Distance.append("사적 모임 가능<br>")
        Distance.append("유흥시설 24시 이후 운영제한<br>")
        Distance.append("식당,카페 운영시간 제한 없음<br>")
        Distance.append("코인노래방 접종증명 시 운영시간 제한 및 인원 제한없음<br>")
        Distance.append("PC방 제한없음<br>")
        Distance.append("헬스장 제한없음<br>")
        Distance.append("영화관 일행 간 한칸 띄우기<br>")

    if level == 2:
        Distance.append("4인까지 모임가능<br>")
        Distance.append("유흥시설 22시 이후 운영제한<br>")
        Distance.append("식당,카페 22시 이후 포장 배달만 허용<br>")
        Distance.append("코인노래방 22시 이후 운영제한<br>")
        Distance.append("PC방 제한없음<br>")
        Distance.append("헬스장 제한없음<br>")

    if level == 3:
        Distance.append("18시 이후 2명까지 모임가능, 18시 이전 4인까지 모임가능<br>")
        Distance.append("유흥시설 집합금지<br>")
        Distance.append("식당,카페 22시 이후 포장 배달만 허용<br>")
        Distance.append("코인노래방 22시 이후 운영제한")
        Distance.append("PC방 22시 이후 운영제한<br>")
        Distance.append("헬스장 22시 이후 운영제한<br>")

    return Distance

print(Junsu(3))


# 전체지역 코로나 단계 출력
def KeepDistanceAllArea():
    target = 3
    print(soup.find(attrs={'class': 'timetable'}).text + " 사회적 거리두기 단계\n\n")
    for descript in soup.find_all("p", "rssd_descript"):
        print(target, "단계")

        area_level[target - 1] = descript.text
        print(area_level[target - 1])

        target -= 1
        if target < 1:
            break
KeepDistanceAllArea()