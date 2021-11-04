#21-11-01 - 김정웅
import requests
from bs4 import BeautifulSoup

# 거리두기 단계 웹 크롤링

def GetPatientRoute():
    try:
        url = requests.get(
            'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=')
        soup = BeautifulSoup(url.content, "html.parser")
        #content > div > div.box_line2 > div > div > table > tbody
        route = soup.select("#content > div > div.box_line2 > div > div > table > tbody > tr")
        print(route)
        for i in range(0, len(route), 1):
            route[i] = route[i].text.replace("소독완료", "").replace("\n", " ")[1:-2]
        for i in range(0, len(route), 1):
            print(i+1,": ",route[i])
        print("해당 시간대에 아래 시설을 방문하신 분은 증상이 없어도 진단검사를 꼭 받아주세요.")
    except:
        print("GetPatientRoute err")

GetPatientRoute()